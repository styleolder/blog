# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from todolist.models import User
from blog.models import blog
from django.utils.encoding import python_2_unicode_compatible
from mptt.models import MPTTModel
from django.utils import timezone
# Create your models here.
# @python_2_unicode_compatible
# class Comment(models.Model):
#     name = models.ForeignKey(User)
#     text = models.TextField()
#     created_time = models.DateTimeField(auto_now_add=True)
#     post = models.ForeignKey(blog)
#     # parent_id = models.CharField(null=True, default=None)
#     class Meta:
#         verbose_name = u'评论'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.text[:20]

@python_2_unicode_compatible
class Comments(MPTTModel):
    text = models.TextField(blank=False, max_length=1024, verbose_name=u'评论内容')
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children",default=None)
    name = models.ForeignKey(User)
    created_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    post = models.ForeignKey(blog)
    last_time = models.DateTimeField(auto_now_add=True,verbose_name='最后更新时间')
    class Meta:
        verbose_name = u'多层评论'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.id)