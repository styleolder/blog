# -*- coding: utf-8 -*-
import xadmin
from todolist.models import TodoList
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class TodoListAdmin(object):
    fields = ('todolist_state', 'todolist_text','pub_date','dodolist_flag')
    list_filter = ['pub_date']
    search_fields = ['todolist_text']
    list_display = ('todolist_text', 'pub_date', 'todolist_state', 'dodolist_flag')
    list_display_links = ('todolist_text', 'pub_date')
    list_editable = ('todolist_state', 'dodolist_flag')


class GlobalSettings(object):
    site_title = u"style的博客"
    site_footer = u"style的博客"
    menu_style = "accordion"


class UsertAdmin(object):
    fields = ('username', 'password', 'email', 'qq', 'last_login', 'user_icon', 'is_active')
    search_fields = ['qq', 'username']
    list_display = ('username', 'email', 'qq', 'last_login', 'is_active', 'user_icon', 'is_active')

xadmin.site.register(TodoList, TodoListAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)