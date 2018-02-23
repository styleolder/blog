# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone
from todolist.models import User
import markdown
from django.utils.html import strip_tags
# from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
#支持python2
@python_2_unicode_compatible
class Category(models.Model):
    #设置字段类型为char,最大长度为20。默认显示名称为 分类
    Category_name = models.CharField(max_length=20, verbose_name=u'分类')

    #多对一关系，反向查找
    #t=Tag.objects.get(pk=1)
    #查询属于这一分类的列表
    #t.blog.set_all()

    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = verbose_name

    #默认返回值,并且在后台有显示信息
    def __str__(self):
        return self.Category_name

class Tag(models.Model):

    Tag_name = models.CharField(max_length=20, verbose_name=u'标签')

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name

    #默认返回值,并且在后台有显示信息
    def __str__(self):
        return self.Tag_name

#支持python2
@python_2_unicode_compatible
class blog(models.Model):
    #blog_content = RichTextUploadingField(verbose_name=u'博客内容')
    #blank=True 默认不能为空
    blog_content = models.TextField(verbose_name=u'博客内容')
    blog_title = models.CharField(max_length=200, verbose_name=u'博客标题')
    created_time = models.DateTimeField(default=timezone.now, verbose_name='博客创建时间')
    modified_time = models.DateTimeField(default=timezone.now, verbose_name='博客修改时间')
    excerpt = models.CharField(max_length=200, blank=True)

    #ForeignKey一对多的关系
    #添加
    #t1=Tag.objects.create(Tag_name="赞助")
    #b=blog.objects.create(blog_content="",blog_title="",tags=t1.....)
    #b.save()

    #删


    #改
    #b=blog.objects.get(id=1)
    #c=category.objects.get(Tag_name="赞助")
    #b.category = c
    #b.save()

    #查

    category = models.ForeignKey(Category)

    #ManyToManyField 多对多的关系,
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User)

    #设置字段为单选项
    # #SHIRT_SIZES = (
    #     ('S', 'Small'),
    #     ('M', 'Medium'),
    #     ('L', 'Large'),
    # )
    # shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

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
    #默认返回值,并且在后台有显示信息
    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'pk': self.pk})

    def __str__(self):
        return self.blog_title

