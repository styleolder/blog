# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from todolist.models import User
from blog.models import blog
from django.utils.encoding import python_2_unicode_compatible
from blog.models import blog
# Create your models here.
@python_2_unicode_compatible
class Comment(models.Model):
    name = models.ForeignKey(User)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(blog)

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text[:20]