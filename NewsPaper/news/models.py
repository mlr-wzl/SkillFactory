from django.db import models
from django.contrib.auth.models import User
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Author(models.Model):  # наследуемся от класса Model
    ranking = models.IntegerField(default=0)
    #author = models.OneToOneField(User, on_delete=models.CASCADE)
    author = models.OneToOneField('auth.User', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=64, default = "No category", unique=True)

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    DATE_INPUT_FORMATS = ["%Y-%m-%d %H:%M:%S.%f"]
    # announcement='Announcement'
    # Posts = [
    #     (announcement, 'Announcement')
    # ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    #type = models.CharField(max_length=15, choices=Posts, default=announcement)
    time = models.DateTimeField(auto_now_add = True)
    category = models.ManyToManyField(Category, through = 'PostCategory')
    title = models.CharField(max_length=100, default='No title')
    text = RichTextUploadingField()
    ranking = models.IntegerField(default = 0)

    def preview(self):
        #return str(self.text)[:124],'...'
        return str(self.text)[:20], '...'


    def __str__(self):
        return f'{self.title.title()}: {self.text[:125]}'


    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'

    # def __str__(self):
    #     return f'{self.title()}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    accepted=models.BooleanField(default = False)



