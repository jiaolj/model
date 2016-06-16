from django.conf.urls import patterns, include, url
from conf.settings import APP_NAME

urlpatterns = patterns('apps.'+APP_NAME+'.analyze.home',
    url(r'^$', 'home'),
)
