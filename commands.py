from news.models import *
from django.contrib.auth.models import User
from django.db import models

# 1: Создать двух пользователей (с помощью метода User.objects.create_user).
user1 = User.objects.create_user(username='User1', email='user1@mail.ru', password='user1')
user2 = User.objects.create_user(username='User2', email='user2@mail.ru', password='user2')

user1 = User.objects.get(id=1)
user2 = User.objects.get(id=2)
# 2: Создать два объекта модели Author, связанные с пользователями.
author1 = Author.objects.create(author=user1)
author2 = Author.objects.create(author=user2)

author1 = Author.objects.get(id=1)
author2 = Author.objects.get(id=2)
# 3: ​Добавить 4 категории в модель Category.
category1=Category.objects.create(name='Love')
category2=Category.objects.create(name='Animals')
category3=Category.objects.create(name='News')
category4=Category.objects.create(name='Children')

# 4: Добавить 2 статьи и 1 новость.
article1 = Post.objects.create(author = author1, type=Post.article, title ='First article', text='This is the text of article 1.')
article2 = Post.objects.create(author = author2, type=Post.article, title ='Second article', text='This is the text of article 2.')
news1 = Post.objects.create(author=author1, type=Post.article, title='First news', text='This is the text of news 1.')

article1 = Post.objects.get(id=1)
article2 = Post.objects.get(id=2)
news1 = Post.objects.get(id=3)

# 5: Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
article1.category.add(category1)
article1.category.add(category2)
article2.category.add(category3)
news1.category.add(category4)

# 6: Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
comment1 = Comment.objects.create(post=article1,user=user1,text='Comment 1')
comment2 = Comment.objects.create(post=article1,user=user1,text='Comment 2')
comment3 = Comment.objects.create(post=article2,user=user1,text='Comment 3')
comment4 = Comment.objects.create(post=news1,user=user2,text='Comment 4')

comment1 = Comment.objects.get(id=1)
comment2 = Comment.objects.get(id=2)
comment3 = Comment.objects.get(id=3)
comment4 = Comment.objects.get(id=4)

# 7: Применяя функции like() и dislike() к статьям/новостям и комментариям,
# скорректировать рейтинги этих объектов.
comment1.like()
comment1.like()
comment1.like()
comment1.like()
comment2.like()
comment2.dislike()
comment2.dislike()
comment3.like()
comment4.like()
article1.like()
article2.like()
news1.dislike()

# 8: Обновить рейтинги пользователей.
author1.update_rating()
author2.update_rating()

# 9: Вывести username и рейтинг лучшего пользователя (применяя сортировку и
# возвращая поля первого объекта).
author_best=Author.objects.order_by('-ranking').first()
Author.objects.filter(id=author_best.id).values()

# 10: Вывести дату добавления, username автора, рейтинг, заголовок и превью
# лучшей статьи, основываясь на лайках/дислайках к этой статье.
post_best=Post.objects.filter(type='Article').order_by('-ranking').first()
Post.objects.filter(id=post_best.id).values()
post_best.preview()

# 11: Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
Comment.objects.filter(post__id=post_best.id).values()









