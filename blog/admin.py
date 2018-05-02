# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from blog.models import Category, Tag, blog, ShortMessage

#扩展后台管理界面
class BlogAdmin(admin.ModelAdmin):
    #fields显示admin界面的字段顺序
    fields = ['blog_title', 'blog_content', 'category', 'tags', 'author', 'created_time', 'excerpt']

    #检索框的搜索范围设置
    search_fields = ['blog_content', 'blog_title', 'author']

    #侧边栏过来字段
    list_filter = ['created_time']

    #默认展示相关的字段
    list_display = (
        'blog_title',
        'author',
        'created_time',
        'modified_time'
    )
    #根据不同的种类信息进行分割显示
    # #fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]
    class Media:
        js = ('/static/js/kindeditor/kindeditor-all-min.js',
              '/static/js/kindeditor/lang/zh-CN.js',
              '/static/js/kindeditor/config.js')

    def make_published(self, request):
        self.message_user(request, "successfully marked as published.")
    actions = [make_published]


admin.site.register(Category)
admin.site.register(Tag)
#注册到后台管理界面
admin.site.register(blog, BlogAdmin)