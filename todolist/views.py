# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import markdown

from models import TodoList


# Create your views here.
def index(request):
    tasks = TodoList.objects.all().order_by("id")
    for task in tasks:
            task.todolist_text = markdown.markdown(task.todolist_text,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'index.html', {"tasks": tasks})
@login_required
def user(request):
     if request.GET:
        word_action = request.GET.get('action')
        if word_action == "add":
            content_text = request.POST['content_text']
            content_time = timezone.localtime(timezone.now()).strftime("%Y-%m-%d %H:%M:%S")
            tasks = TodoList.objects.create(todolist_text=content_text, pub_date=content_time, todolist_state=1, dodolist_flag=0)
            tasks.save()
        elif word_action == "del":
            word_id = request.GET.get('id')
            TodoList.objects.get(id=word_id).delete()
        else:
            pass
     return HttpResponseRedirect('/todolist')

def status(request):
     if request.GET:
        state_id = request.GET.get('id')
        todolist_status = request.GET.get('code')
        TodoList.objects.filter(id=state_id).update(todolist_state=todolist_status)
     return HttpResponseRedirect('/todolist')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        next_page = request.POST.get('next', '/')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(next_page)
    return render(request, 'login.html')

def zone(request):
    return render(request, 'zone.html')

@login_required
def logout(request):
    auth.logout(request)
    next_page = request.GET.get('next', '/')
    ##BUG
    return HttpResponseRedirect(next_page)