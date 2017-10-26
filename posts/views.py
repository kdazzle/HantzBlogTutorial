from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post


def index(request):
    template = loader.get_template('posts/index.html')
    context = {
        'posts': Post.objects.all(),
    }
    print("Hello there")
    print("Another one")
    return HttpResponse(template.render(context, request))
