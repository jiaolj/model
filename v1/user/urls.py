from django.conf.urls import patterns, url

urlpatterns = patterns('user.home',
    url(r'^get', 'get'),
    url(r'^login', 'login'),
    url(r'^logout', 'logout'),
)