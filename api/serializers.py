# -*- coding: utf-8 -*-
__author__ = 'admin'
from rest_framework import serializers
from blog.models import blog, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = blog
        fields = "__all__"