from django.urls import path
from .views import *  # импортируем наше представление


urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', NewsList.as_view()),
    path('<int:pk>', (NewsDetailView.as_view()), name='news_detail'),
    path('create/', NewsCreateView.as_view(), name='news_create'),  # Ссылка на создание товара
    path('update/<int:pk>', NewsUpdateView.as_view(), name='news_update'),
    path('delete/<int:pk>', NewsDeleteView.as_view(), name='news_delete'),
    path('comment/', NewsCommentView.as_view(), name='comment_create'),
    path('mycomments', CommentsList.as_view(), name='mycomments'),
    path('deletecomment/<int:pk>', CommentDeleteView.as_view(), name='comment_delete'),
    path('accept/<int:pk>/', Accept.as_view(), name='accept'),
    path('filter/<int:pk>', CommentFilterView.as_view(), name='comment_filter'),
]
