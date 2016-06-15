from django.conf.urls import patterns, include, url
from conf.settings import STATIC_ROOT

urlpatterns = patterns('',
    url(r'^$', include('default.urls')),
    url(r'^user/', include("user.urls")),
)
#urlpatterns += patterns('',url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': STATIC_ROOT,}),)
urlpatterns += patterns('',url(r'^(?P<path>.*)$', 'django.views.static.serve', { 'document_root': STATIC_ROOT,}),)