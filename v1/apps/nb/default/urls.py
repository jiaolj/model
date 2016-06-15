from django.conf.urls import patterns, url
from conf.settings import APP_NAME

urlpatterns = patterns('apps.'+APP_NAME+'.default.home',
    url(r'^$', 'home'),
)