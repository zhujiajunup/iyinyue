from django.db import models
from django.utils import timezone


# 音乐类别表
class MusicCategory(models.Model):
    music_category = models.CharField(max_length=100)


# 音乐表
class Music(models.Model):
    song_name = models.CharField(max_length=100)  # 歌曲名
    album = models.CharField(max_length=100, blank=True, null=True)  # 专辑
    year = models.CharField(max_length=100, blank=True, null=True)  # 年代
    artist = models.CharField(max_length=100, blank=True, null=True)  # 歌手
    comment = models.CharField(max_length=100, blank=True, null=True)  # 备注
    genre = models.CharField(max_length=100, blank=True, null=True)  # 类型
    path = models.CharField(max_length=100, blank=True, null=True)  # 文件路径
    category = models.ManyToManyField(MusicCategory, blank=True, null=True, related_name="category")  # 分类
    popular = models.IntegerField(default=0)  # 流行度
    unpopular = models.IntegerField(default=0)  # 不受欢迎度

    def __str__(self):
        return 'song_name:'+self.song_name + \
               'artist:'+self.artist + \
               '<'+self.album+'>'


# 对歌曲播放次数
class PlayTime(models.Model):
    music = models.ForeignKey(Music)  # 对应歌曲
    play_time = models.IntegerField(blank=True, null=True, default=0)  # 播放次数
    add_date = models.DateTimeField('add_date', blank=True, null=True)  # 歌曲添加的时间


class PlayList(models.Model):
    play_list_name = models.CharField(max_length=100)  # 列表名称
    play_time = models.ManyToManyField(PlayTime,  blank=True, null=True,
                                       related_name="musics")  # 列表歌曲播放情况


# 音乐平台用户表
class IUser(models.Model):
    user_name = models.CharField(max_length=100)  # 用户昵称
    birthday = models.DateField('birthday', blank=True, null=True)  # 用户生日
    password = models.CharField(max_length=100)  # 密码
    sex = models.IntegerField(blank=True, null=True, default=1)  # 性别 男：true；女：false
    email = models.EmailField(max_length=100, blank=True, null=True)  # 邮箱
    tag = models.CharField(max_length=200, blank=True, null=True)  # 标签 允许为空
    head_img = models.CharField(max_length=100, blank=True, null=True)  # 头像
    register_time = models.DateField(blank=True, null=True, default=timezone.now())  # 注册时间
    last_time = models.DateField(blank=True, null=True)  # 最后一次登入时间
    play_recorded = models.ManyToManyField(PlayTime, blank=True, null=True,
                                           related_name="play_recorded")  # 播放历史记录
    play_list = models.ManyToManyField(PlayList, blank=True, null=True,
                                       related_name='play_list')  # 播放列表
    favorite_songs = models.ManyToManyField(PlayTime, blank=True, null=True,
                                            related_name="favorite_songs")  # 收藏列表
    dislike_songs = models.ManyToManyField(Music, blank=True, null=True,
                                           related_name="dislike_songs")  # dislike歌曲列表
    friends = models.ManyToManyField('self', blank=True, null=True, related_name='friends')  # 好友

    def __str__(self):
        return self.user_name


# 推荐的项目
class RecommendItem(models.Model):
    music = models.ForeignKey(Music)  # 推荐的歌曲
    recommend_date = models.DateTimeField('recommend_date', default=timezone.now)  # 推荐的时间


# 推荐的历史记录表
class RecommendHistory(models.Model):
    recommend_user = models.ForeignKey(IUser)  # 推荐的目标用户
    latest_recommend_time = models.DateTimeField()  # 最新一次推荐时间
    # 推荐的歌曲列表 many-to-many
    recommend_items = models.ManyToManyField(RecommendItem, blank=True, null=True, related_name='recommend_item')


# 用户为歌曲打标签表
class MusicTag(models.Model):
    tag_user = models.ForeignKey(IUser)  # 标记用户
    tag_music = models.ForeignKey(Music)  # 用户标记的歌曲
    tag_time = models.DateField('tag_time', default=timezone.now())  # 标记操作时间
    tag_content = models.CharField(max_length=100)  # 标记内容

    def __str__(self):
        return self.tag_user.user_name+','+self.tag_music.song_name+','+self.tag_time.__str__()+','+self.tag_content


# 用户相关操作表
class Operation(models.Model):
    operation_user = models.ForeignKey(IUser)
    operation_music = models.ForeignKey(Music)
    operation_time = models.DateField('operation_time')
    operation_type = models.CharField(max_length=50)

    def __str__(self):
        return 'operation_user:'+self.operation_user.user_name + \
               'operation_type:' + self.operation_type + \
               'operation_music:'+self.operation_music.song_name
