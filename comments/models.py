# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from todolist.models import User
from blog.models import blog
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
@python_2_unicode_compatible
class Comment(models.Model):
    name = models.OneToOneField(User)
    user_icon = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(blog)

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text[:20]