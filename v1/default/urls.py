from django.conf.urls import patterns, url

urlpatterns = patterns('default.home',
    url(r'^$', 'home'),
)