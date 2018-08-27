from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Tags(models.Model):
    tag_name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.tag_name


class Article(models.Model):
    description= models.CharField(max_length=255)
    last_update = models.DateTimeField(auto_now_add=True)
    tag_name=models.ForeignKey(Tags,on_delete=models.CASCADE,related_name='Article')
    starter = models.ForeignKey(User, on_delete=models.CASCADE,related_name='Article')


class Comment(models.Model):
    message = models.TextField(max_length=4000)
    article_name = models.ForeignKey(Article, on_delete=models.CASCADE,related_name='Comment')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Comment')


# Create your models here.
