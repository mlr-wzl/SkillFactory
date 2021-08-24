from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import *


# создаём фильтр
class NewsFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах
    class Meta:
        model = Post
        fields = {
            'time' :  ['gt'], # default input format: 2021-05-26 16:00:00
            'title': ['icontains'],
            'author__author__username': ['icontains'],
        }

class CommentsFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах
    class Meta:
        model = Comment
        fields = {
            'text': ['icontains'],
        }