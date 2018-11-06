from django.conf.urls import url, include
from django.urls import path
from django.views.generic import ListView, DetailView
from .models import Post
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
