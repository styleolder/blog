# -*- coding: utf-8 -*-
from blog.models import blog
from .serializers import BlogSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


class BaseSetPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 10
    page_size_query_param = 'page_size'


class BlogList(generics.ListAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = BaseSetPagination