from django.urls import path
from .views import *  # импортируем наше представление



urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', NewsList.as_view()),
    #path('<int:pk>', NewsDetail.as_view()),
    path('search', NewsSearchList.as_view()),
    # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('create/', NewsCreateView.as_view(), name='news_create'),  # Ссылка на создание товара
    path('update/<int:pk>', NewsUpdateView.as_view(), name='news_update'),
    path('delete/<int:pk>', NewsDeleteView.as_view(), name='news_delete'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
]