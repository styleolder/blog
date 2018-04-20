# -*- coding: utf-8 -*-
from rest_framework.decorators import api_view
from blog.models import blog
from api.serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class BlogList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = blog.objects.all()
        serializer = BlogSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

