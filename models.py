from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):  # наследуемся от класса Model
    ranking = models.IntegerField(default=0)
    author = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        author_posts = Post.objects.filter(author = self.id, type = 'Article')
        total_post_ranking = 0
        for post in author_posts:
            total_post_ranking += post.ranking * 3

        total_authcomment_ranking = 0
        author_comments = Comment.objects.filter(user= self.author)
        for comment in author_comments:
            total_authcomment_ranking += comment.ranking

        total_postcomment_ranking = 0
        authposts_comments = Comment.objects.filter(post__author=self.id, post__type = 'Article')
        for comment in authposts_comments:
            total_postcomment_ranking += comment.ranking

        self.ranking = total_postcomment_ranking + total_authcomment_ranking + total_post_ranking
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, default = "No category", unique=True)


class Post(models.Model):
    news='News'
    article='Article'
    Posts = [
        (news, 'News'),
        (article, 'Article')
    ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=Posts, default=news)
    time = models.DateTimeField(auto_now_add = True)
    category = models.ManyToManyField(Category, through = 'PostCategory')
    title = models.CharField(max_length=100, default='No title')
    text = models.TextField()
    ranking = models.IntegerField(default = 0)

    def like(self):
        self.ranking += 1
        self.save()

    def dislike(self):
        self.ranking -= 1
        self.save()

    def preview(self):
        return str(self.text)[:124],'...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    ranking = models.IntegerField(default=0)

    def like(self):
        self.ranking += 1
        self.save()

    def dislike(self):
        self.ranking -= 1
        self.save()



