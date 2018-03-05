# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import blog
from api.serializers import BlogSerializer
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET', 'POST'])
@csrf_exempt
def blog_list(request):
    """
    列出所有的代码片段（snippets），或者创建一个代码片段（snippet）
    """
    if request.method == 'GET':
        snippets = blog.objects.all()
        serializer = BlogSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def blog_detail(request, pk):
    """
    读取, 更新 或 删除 一个代码片段实例（snippet instance）。
    """
    try:
        snippet = blog.objects.get(pk=pk)
    except blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BlogSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
