from __future__ import unicode_literals

from django.db import models


class Post(models.Model):

    date_published = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=64)
