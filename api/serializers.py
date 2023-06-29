from rest_framework import serializers
from blog.models import Category,Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')
