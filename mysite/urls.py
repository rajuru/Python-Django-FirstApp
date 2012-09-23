from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^polls/$', 'polls.views.index'),
  url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
  url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
  url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^topics/$', 'newscred.views.index'),
  url(r'^topics/(?P<topic_guid>\w+)/$', 'newscred.views.detail'),
  url(r'^topics/(?P<topic_guid>\w+)/update/$', 'newscred.views.update'),
)

urlpatterns += staticfiles_urlpatterns()
