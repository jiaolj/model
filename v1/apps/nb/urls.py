from django.conf.urls import patterns, include, url
from conf.settings import APP_NAME
from conf.urls import urlpatterns

urlpatterns += patterns('apps.'+APP_NAME+'.home',
    url(r'^$', 'home'),
)
urlpatterns += patterns('apps.'+APP_NAME+'.es',
    url(r'^es/get/$', 'get'),
    url(r'^es/list/$', 'test'),
)
urlpatterns += patterns('',
    url(r'^analyze/', include('apps.'+APP_NAME+'.analyze.urls')),
    url(r'^custom/', include('apps.'+APP_NAME+'.custom.urls')),
)
handler404 = 'common.views.error.page_not_found'
handler500 = 'common.views.error.page_error'