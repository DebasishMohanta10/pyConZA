from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer
from blog.models import Category,Post


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class=PostSerializer
