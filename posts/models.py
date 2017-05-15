from django.db import models


class Post(models.Model):

    date_published = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=64)

    def __str__(self):
        return self.title
