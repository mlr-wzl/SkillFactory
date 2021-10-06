
from django.urls import path, re_path
from .views import index, room
from . import views

app_name='chat'

urlpatterns = [
    path('', index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]