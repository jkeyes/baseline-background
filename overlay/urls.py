from django.conf.urls import include, url
from overlay import views
urlpatterns = [
    url(r'^$', views.overlay, name='home')
]
