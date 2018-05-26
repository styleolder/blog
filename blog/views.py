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
from braces.views import SetHeadlineMixin

class IndexView(ListView):
    model = blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs'
    paginate_by = 5


class PostView(SetHeadlineMixin,DetailView):
    model = blog
    template_name = 'blog/post.html'
    context_object_name = 'blogs'
    headline = u"This is our headline"

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
            previous_post = post_list[idx - 1 if idx > 1 else None]
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


class TagsView(ListView):
    model = blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_queryset(self):
        tags = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagsView, self).get_queryset().filter(tags=u'tags')


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
