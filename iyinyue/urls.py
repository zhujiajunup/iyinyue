from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^index/$', 'iyinyue.views.index', name='index'),
                       url(r'^genres/$', 'iyinyue.views.genres', name='genres'),
                       url(r'^404/$', 'iyinyue.views.not_found', name='404'),
                       # Examples:
                       url(r'^listen/$', 'iyinyue.views.listen', name='listen'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^user/', include('user.urls', namespace='user')),
                       url(r'^music/', include('music.urls', namespace='music')),
                       # url(r'^admin/', include(admin.site.urls)),
                       )
