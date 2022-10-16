from django import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
import videos

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/videos', views.videos),
    url(r'^api/like_video/(?P<video_id>[0-9]+)$', views.like_video)
]