from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


class Author(models.Model):  # наследуемся от класса Model
    ranking = models.IntegerField(default=0)
    author = models.OneToOneField('auth.User', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=64, default = "No category", unique=True)

    def __str__(self):
        return f'{self.name}'


class Video(models.Model):
    title=models.CharField(max_length=100)
    added=models.DateTimeField(auto_now_add=True)
    url=EmbedVideoField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    category = models.ManyToManyField(Category, through='VideoCategory')
    likesCount = models.IntegerField(default=0)
    subscribers = models.ManyToManyField(User)

    def like(self):
        self.likesCount += 1
        self.save()

    def dislike(self):
        self.likesCount -= 1
        self.save()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering=['-added']


class VideoCategory(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    accepted=models.BooleanField(default = False)



