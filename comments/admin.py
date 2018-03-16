# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Comment
from django.contrib import admin

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    #fields显示admin界面的字段顺序
    fields = ['parent', 'text', 'post', 'name']
    #侧边栏过来字段
    list_filter = ['created_time']
    #默认展示相关的字
    list_display = (
        'id',
        'name',
        'text',
        'created_time',
        'parent',
    )
    class Media:
        js = ('/static/js/kindeditor/kindeditor-all-min.js',
              '/static/js/kindeditor/lang/zh-CN.js',
              '/static/js/kindeditor/config.js')
admin.site.register(Comment, CommentAdmin)
