from django.conf.urls import url, include

from posts import views

urlpatterns = [
    url(r'^$', views.index),
]