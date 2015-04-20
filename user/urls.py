__author__ = 'Administrator'
from django.conf.urls import patterns, url
from user import views

urlpatterns = patterns('',
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.login, name='login'),
                       url(r'^getUserInfo/$', views.get_user_info, name='getUserInfo'),
                       # url(r'register1/$', views.signup, name='hello'),
                       # url(r'hello/test/$', views.test, name='test'),
)
