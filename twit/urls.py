from django.contrib import admin
from django.conf.urls import patterns, include, url
from mysite.api import EntryResource
from mysite import views
entry_resource = EntryResource()

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(entry_resource.urls)),
    url(r'^crawl/$', 'mysite.views.crawl'),
    url(r'^$', 'mysite.views.index'),
    )

urlpatterns += patterns(
    'django.contrib.staticfiles.views',
    url(r'^(?:index.html)?$', 'serve', kwargs={'path': 'index.html'}),
    url(r'^(?P<path>(?:js|css|img)/.*)$', 'serve'),
)