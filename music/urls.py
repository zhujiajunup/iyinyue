__author__ = 'Administrator'
from django.conf.urls import patterns, url
from music import views

urlpatterns = patterns('',
                       # 获取用户播放列表url
                       url(r'^playlist/$', views.get_play_list, name='get_play_list'),
                       # 添加音乐到播放列表url
                       url(r'^addToList/$', views.add_to_playlist, name='add_to_playlist'),
                       # 用户下载操作url
                       url(r'^download/$', views.download, name='download'),
                       # 用户标记红心操作url
                       url(r'^heart/$', views.heart_operation, name='heart'),
                       # 用户踩操作url
                       url(r'^dislike/$', views.dislike_operation, name='dislike'),
                       # 初始化音乐（存储数据库）url
                       url(r'^init_music/$', views.init_music, name='initmusic'),
                       # 获取所有音乐列表url
                       url(r'^all/$', views.get_all, name='all'),
                       # 推荐歌曲url
                       url(r'^recommend/$', views.recommend, name='recommend'),
                       # 根据歌曲风格类别来获取音乐
                       url(r'^getByGenre/$', views.get_music_by_genre, name='getByGenre'),
                       )