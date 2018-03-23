# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from todolist.models import User
from django.utils.encoding import python_2_unicode_compatible
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from blog.models import blog
# Create your models here.
@python_2_unicode_compatible
class Comment(MPTTModel):
    name = models.ForeignKey(User)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    post = models.ForeignKey(blog)

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = verbose_name

    class MPTTMeta:
        order_insertion_by = ['created_time']

    def __str__(self):
        return str(self.pk)