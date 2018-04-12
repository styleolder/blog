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
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
from django import forms
from braces.views import SetHeadlineMixin

class IndexView(SetHeadlineMixin, ListView):
    model = blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_headline(self):
        return u'首页'


class PostView(SetHeadlineMixin, DetailView):
    model = blog
    template_name = 'blog/post.html'
    context_object_name = 'blogs'

    def get_object(self, queryset=None):
        blogs = super(PostView, self).get_object(queryset=queryset)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify=slugify),
        ])
        blogs.blog_content = md.convert(blogs.blog_content)
        blogs.toc = md.toc
        return blogs


    def get_headline(self):
        if self.object.category:
            return '%s_%s' % (self.object.blog_title, self.object.category.Category_name)
        return '%s' % self.object.blog_title


    def get_context_data(self, **kwargs):
        context = super(PostView,self).get_context_data(**kwargs)
        post = self.object

        try:
            previous_post = post.get_previous_by_created_time()
        except blog.DoesNotExist:
            previous_post = None

        try:
            next_post = post.get_next_by_created_time()
        except blog.DoesNotExist:
            next_post = None
        self.template_name = 'blog/post.html'
        post_list = list(blog.objects.all().order_by('-created_time'))
        context['post_list'] = post_list
        idx = post_list.index(post)
        try:
            previous_post = post_list[idx-1 if idx >= 1 else None]
        except (IndexError, TypeError):
            previous_post = None

        try:
            next_post = post_list[idx + 1]
        except IndexError:
            next_post = None
        context['previous_post'] = previous_post
        context['next_post'] = next_post

        return context

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


class TagsView(SetHeadlineMixin, ListView):
    model = blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_queryset(self):
        tags = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagsView, self).get_queryset().filter(tags=tags)

    def get_headline(self):
        tags = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        if tags:
            return '%s' % tags
        return u'分类'


class CategoryView(SetHeadlineMixin, ListView):
    model = blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)

    def get_headline(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        if cate:
            return '%s' % cate
        return u'分类'


class UserView(ListView):
    model = blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_queryset(self):
        user_id = get_object_or_404(User, pk=self.kwargs.get('pk'))
        return super(UserView, self).get_queryset().filter(author=user_id)


class AddForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField()

def login(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
            return HttpResponseRedirect('/blog')
        return render(request, 'blog/login.html')
    if request.method == 'GET':
        return render(request, 'blog/login.html')


@login_required(login_url="/blog/login")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/blog')
