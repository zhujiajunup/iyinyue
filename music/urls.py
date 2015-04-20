__author__ = 'Administrator'
from django.conf.urls import patterns, url
from music import views

urlpatterns = patterns('',
                       # 获取用户播放列表url
                       url(r'^playlist/$', views.get_play_list, name='get_play_list'),
                       # 添加音乐到播放列表url
                       url(r'^addToList/$', views.add_to_playlist, name='add_to_playlist'),
                       url(r'^download/$', views.download, name='download'),
                       url(r'^heart/$', views.heart_operation, name='heart'),
                       url(r'^dislike/$', views.dislike_operation, name='dislike'),
                       url(r'^init_music/$', views.init_music, name='initmusic'),
                       url(r'^all/$', views.get_all, name='all'),
                       )