from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=10)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    e_mail = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.content


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.content
