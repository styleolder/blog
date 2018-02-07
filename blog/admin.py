# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Category, Tag, blog


class BlogAdmin(admin.ModelAdmin):
    fields = ('blog_title', 'blog_content', 'category', 'tags', 'author', 'created_time', 'modified_time', 'excerpt')
    search_fields = ['blog_content', 'blog_title', 'author']
    list_filter = ['created_time']
    list_display = (
        'blog_title',
        'author',
        'created_time'
    )
    class Media:
        js = ('/static/js/kindeditor/kindeditor-all-min.js',
              '/static/js/kindeditor/lang/zh-CN.js',
              '/static/js/kindeditor/config.js')

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(blog, BlogAdmin)