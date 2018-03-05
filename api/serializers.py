__author__ = 'admin'
from rest_framework import serializers
from blog.models import blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = ('id', 'blog_title', 'blog_content', 'created_time')
