from django.conf.urls import url, include
from django.urls import path
from django.views.generic import ListView, DetailView
from .models import Post
from . import views

urlpatterns = [
    url(r'^$', ListView.as_view(
                        queryset=Post.objects.all().order_by("-date")[:25],
                        template_name="posts/posts.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(
                        model = Post,
                        template_name="posts/post.html")),
]
