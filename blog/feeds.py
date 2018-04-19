# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from blog.models import blog

class AllPostsRssFeed(Feed):
    # 显示在聚合阅读器上的标题
    title = "Django 博客教程演示项目"

    # 通过聚合阅读器跳转到网站的地址
    link = "/blog/list/"

    # 显示在聚合阅读器上的描述信息
    description = "Django 博客教程演示项目测试文章"

    # 需要显示的内容条目
    def items(self):
        return blog.objects.all()

    # 聚合器中显示的内容条目的标题
    def item_title(self, item):
        return '[%s] %s' % (item.blog_title, item.tags)

    # 聚合器中显示的内容条目的描述
    def item_description(self, item):
        return item.blog_content


    def item_link(self, item):
        return reverse('blog:post', args=[item.id])