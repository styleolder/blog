# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Comment
from django.contrib import admin

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    #fields显示admin界面的字段顺序
    fields = ['text', 'post', 'name','user_icon']
    #侧边栏过来字段
    list_filter = ['created_time']
    #默认展示相关的字段
    list_display = (
        'name',
        'text',
        'created_time',
        'user_icon',
    )
admin.site.register(Comment, CommentAdmin)
