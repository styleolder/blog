# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone
from todolist.models import User
import markdown
from django.utils.html import strip_tags
from ckeditor_uploader.fields import RichTextUploadingField

@python_2_unicode_compatible
class Category(models.Model):
    Category_name = models.CharField(max_length=20, verbose_name=u'分类')

    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Category_name

class Tag(models.Model):
    Tag_name = models.CharField(max_length=20, verbose_name=u'标签')

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Tag_name

@python_2_unicode_compatible
class   blog(models.Model):
    #blog_content = RichTextUploadingField(verbose_name=u'博客内容')
    blog_content = models.TextField(verbose_name=u'博客内容')
    blog_title = models.CharField(max_length=200, verbose_name=u'博客标题')
    created_time = models.DateTimeField(default=timezone.now, verbose_name='博客创建时间')
    modified_time = models.DateTimeField(default=timezone.now, verbose_name='博客修改时间')
    excerpt = models.CharField(default=1, max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)

    class Meta:
        verbose_name = u'博客信息'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.blog_content))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.blog_title

