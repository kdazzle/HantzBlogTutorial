from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from posts.models import Post


def index(request):
    template = loader.get_template('posts/index.html')
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))
