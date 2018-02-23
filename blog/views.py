# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
import markdown
from models import blog, Tag, Category
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from todolist.models import User
class IndexView(ListView):
    model = blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs'
    paginate_by = 5

class PostView(DetailView):
    model = blog
    template_name = 'blog/post.html'
    context_object_name = 'blogs'

    def get_object(self):
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        blogs = super(PostView, self).get_object(queryset=None)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        blogs.blog_content = md.convert(blogs.blog_content)
        blogs.toc = md.toc
        return blogs

class ArchivesView(ListView):
    model = blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_queryset(self):
        year = int(self.kwargs.get('year'))
        month = int(self.kwargs.get('month'))
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year,
                                                               created_time__month=month
                                                               )
class TagsView(ListView):
    model = blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_queryset(self):
        tags = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagsView, self).get_queryset().filter(tags=tags)


class CategoryView(ListView):
    model = blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)

class UserView(ListView):
    model = blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_queryset(self):
        user_id = get_object_or_404(User, pk=self.kwargs.get('pk'))
        return super(UserView, self).get_queryset().filter(author=user_id)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/blog')
    return render(request, 'blog/index.html')

@login_required(login_url="/blog")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/blog')