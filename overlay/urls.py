from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'overlay.views.overlay', name='home')
)
