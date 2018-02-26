# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import TodoList, User


class TodoListAdmin(admin.ModelAdmin):
    fields = ('todolist_state', 'todolist_text','pub_date','dodolist_flag')
    list_filter = ['pub_date']
    search_fields = ['todolist_text']
    list_display = ('todolist_text', 'pub_date', 'todolist_state', 'dodolist_flag')
    list_display_links = ('todolist_text', 'pub_date')
    list_editable = ('todolist_state', 'dodolist_flag')

class UsertAdmin(admin.ModelAdmin):
    fields = ('username', 'password', 'email', 'qq', 'last_login','user_icon')
    search_fields = ['qq']
    list_display = ('username', 'email', 'qq', 'last_login', 'is_active','user_icon')

admin.site.register(TodoList, TodoListAdmin)
admin.site.register(User, UsertAdmin)