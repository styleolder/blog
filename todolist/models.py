# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

@python_2_unicode_compatible
class TodoList(models.Model):
    todolist_text = models.TextField(max_length=200, verbose_name=u'任务内容')
    pub_date = models.DateTimeField(default=timezone.now, verbose_name='任务发布时间')
    todolist_state = models.IntegerField(verbose_name=u'任务状态')
    dodolist_flag = models.IntegerField(verbose_name=u'是否删除')

    class Meta:
        verbose_name = u'任务列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.todolist_text

@python_2_unicode_compatible
class User(AbstractUser):
    username = models.CharField(max_length=200, verbose_name=u'用户名', blank=False, unique=True)
    qq = models.IntegerField(null=True, verbose_name='QQ', blank=False, unique=True)
    email = models.CharField(null=True, max_length=200, verbose_name=u'邮件', blank=False, unique=True)
    user_icon = models.ImageField(upload_to="images/%Y/%m", default=u"image/default.png", max_length=500)
    class Meta(AbstractUser.Meta):
        verbose_name = u'用户'
        verbose_name_plural = verbose_name
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.username