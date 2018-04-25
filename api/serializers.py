# -*- coding: utf-8 -*-
__author__ = 'admin'
from rest_framework import serializers
from blog.models import blog, Category
from todolist.models import User
from rest_framework import viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff', 'user_icon')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(pk__gt=10)
    serializer_class = UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = blog
        fields = "__all__"

class BlogViewSet(viewsets.ModelViewSet):
    queryset = blog.objects.all()
    serializer_class = BlogSerializer