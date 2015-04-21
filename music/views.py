from django.http import *
from user.models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone
import json
from iyinyue.utils import filedir, mp3reader
import mutagen.mp3


# 获取登录用户的歌曲列表
def get_play_list(request):
    user = IUser.objects.get(user_name=request.GET.get('user_name', None))
    play_lists = user.play_list.all()
    play_list_json = []
    for play_list in play_lists:
        play_times = play_list.play_time.all()
        for play_time in play_times:
            music = play_time.music
            music_json = {
                'id': music.id,
                'title': music.song_name,
                'artist': music.artist,
                'mp3': music.path,
                'poster': "images/m0.jpg"
            }
            play_list_json.append(music_json)
    return HttpResponse(json.dumps(play_list_json), content_type='application/json')


# 获取数据库中所有歌曲
def get_all(request):
    play_list = Music.objects.all()
    play_list_json = []
    for music in play_list:
        music_json = {
            'id': music.id,
            'title': music.song_name,
            'artist': music.artist,
            'mp3': music.path,
            'poster': "images/m0.jpg"
        }
        play_list_json.append(music_json)
    return HttpResponse(json.dumps(play_list_json), content_type='application/json')


# 添加音樂到播放列表
def add_to_playlist(request):
    music_id = request.POST.get('music_id', None)
    play_list_id = request.POST.get('list_id', None)
    # play_list = PlayList.objects.get(pk=1)  # TODO 获取播放列表
    play_list = PlayList.objects.filter(pk=play_list_id, play_time__music__id=music_id)
    # user = IUser.objects.filter(play_list__id=1,
    #                             play_list__play_time__music__id=music_id)\
    #     .filter(user_name=user_name)  # 查找个用户是否已经添加了该歌曲
    if not play_list.exists():  # 用户不存在，则添加该歌曲到用户的播放列表
        # user = IUser.objects.get(user_name=user_name)  # 获取用户
        try:
            music = Music.objects.get(pk=music_id)  # 获取音乐
            play_list = PlayList.objects.get(pk=play_list_id)  # 获取播放列表
            play_time = PlayTime()
            play_time.music = music
            play_time.save()
            play_list.play_time.add(play_time)
            play_list.save()
            music.popular += 1  # 播放次数+1
            music.save()
            return HttpResponse('successful')
        except Music.DoesNotExist:
            HttpResponse('音乐不存在')
        except PlayList.DoesNotExist:
            HttpResponse('播放列表不存在')

    return HttpResponse('already added to you list')


# 用户下载操作
def download(request):
    try:
        music = Music.objects.get(pk=request.POST.get('music_id', None))
        user = IUser.objects.get(user_name=request.POST.get('user_name', None))

    except(Music.DoesNotExist, IUser.DoesNotExist):
        return HttpResponse('failed')
    else:
        operation_time = timezone.now()
        operation_type = 'download'
        operation = Operation(operation_time=operation_time,
                              operation_type=operation_type,
                              operation_user=user,
                              operation_music=music)
        operation.save()
        return HttpResponse('successful')


# 用户标记红心操作
def heart_operation(request):
    try:
        music = Music.objects.get(pk=request.POST.get('music_id', None))
        user = IUser.objects.get(user_name=request.POST.get('user_name', None))

    except(Music.DoesNotExist, IUser.DoesNotExist):
        return HttpResponse('failed')
    else:
        operation_time = timezone.now()
        operation_type = 'heart'
        operation = Operation(operation_time=operation_time,
                              operation_type=operation_type,
                              operation_user=user,
                              operation_music=music)
        user.favorite_songs.add(music)
        operation.save()
        user.save()
        return HttpResponse('successful')


# 用户分享音乐操作
def share_operation(request):
    try:
        music = Music.objects.get(pk=request.POST.get('music_id', None))
        user = IUser.objects.get(user_name=request.POST.get('user_name', None))

    except(Music.DoesNotExist, IUser.DoesNotExist):
        return HttpResponse('failed')
    else:
        operation_time = timezone.now()
        operation_type = 'heart'
        operation = Operation(operation_time=operation_time,
                              operation_type=operation_type,
                              operation_user=user,
                              operation_music=music)
        operation.save()
        return HttpResponse('successful')


# 用户踩操作
def dislike_operation(request):
    try:
        music = Music.objects.get(pk=request.POST.get('music_id', None))
        user = IUser.objects.get(user_name=request.POST.get('user_name', None))
    except(Music.DoesNotExist, IUser.DoesNotExist):
        return HttpResponse('failed')
    else:
        operation_time = timezone.now()
        operation_type = 'dislike'
        operation = Operation(operation_time=operation_time,
                              operation_type=operation_type,
                              operation_user=user,
                              operation_music=music)
        operation.save()
        music.unpopular += 1  # 踩一下
        music.save()  # 保存
        return HttpResponse('successful')


# 用户对歌曲打标签操作
def tag_music(request):
    if request.method == 'POST':  # 方法为POST
        try:
            music = Music.objects.get(pk=request.POST.get('music_id', None))
            user = IUser.objects.get(user_name=request.POST.get('user_name', None))
            tag_content = request.POST.get('tag', None)  # 获取tag信息
        except(Music.DoesNotExist, IUser.DoesNotExist):
            return HttpResponse('failed')
        else:
            music_tag = MusicTag()
            music_tag.tag_content = tag_content
            music_tag.tag_music = music
            music_tag.tag_user = user
            music_tag.save()
            return HttpResponse('successful')


# 批量添加音乐
def init_music(request):
    path = 'G:/iyinyue/iyinyue/static/iyinyue/mp3'
    all_files = filedir.print_path(path)
    for file in all_files:
        if 'mp3' not in file:
            continue
        try:
            info = mp3reader.get_mp3_info(file)
        except mutagen.mp3.HeaderNotFoundError:
            continue
        music = Music()
        print(info)
        for k, v in info.items():
            for va in v:
                value = va+' '
            if 'title' == k:
                music.song_name = str(value).strip()
            if 'artist' == k:
                music.artist = str(value).strip()
            if 'album' == k:
                music.album = str(value).strip()
            if 'genre' == k:
                music.genre = str(value).strip()
            if 'year' == k:
                music.year = str(value).strip()
            if 'comment' == k:
                music.comment = str(value).strip()
        music.path = file.replace('G:/iyinyue/iyinyue/', 'http://127.0.0.1:8000/')
        music.save()


# 个性化音乐推荐
def recommend(request):
    return None


# 根据风格类型来获取音乐列表
def get_music_by_genre(request):
    return None

if __name__ == '__main__':
    init_music(request=None)