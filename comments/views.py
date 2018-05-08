# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from comments.models import Comment
from blog.models import blog
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from todolist.models import User
# Create your views here.

def reply_comment(request, pk):
    if request.user.is_authenticated():
        reply_comment_username = request.user
    else:
        reply_comment_username = User.objects.get(username="匿名用户")

    if request.method == 'POST':
        reply_comment_content = request.POST.get('my-edit-html-code')
        if reply_comment_content is None:
            reply_comment_content = request.POST.get('my-edit-default-html-code')
        reply_comment_next = request.POST.get('next', 'value')
        reply_comment_post = request.POST.get('post', 'value')
        if reply_comment_content is not None:
            if int(pk) == 0:
                find_comment = None
                comment_post = blog.objects.get(id=reply_comment_post)
            else:
                find_comment = Comment.objects.get(id=pk)
                comment_post = find_comment.post
            try:
                keep_comment = Comment.objects.create(name=reply_comment_username,
                                                  text=reply_comment_content,
                                                  parent=find_comment,
                                                  post=comment_post)
                keep_comment.save()
            except Exception, e:
                print e
        return HttpResponseRedirect(reply_comment_next)
    return HttpResponseRedirect('/blog')

@login_required(login_url="/blog/user_login")
@csrf_exempt
def remove_comment(request, pk):
    if request.user == Comment.objects.get(id=pk).name:
        try:
            Comment.objects.get(id=pk).delete()
            return JsonResponse({'res': 1})
        except Exception, e:
            print e
            return JsonResponse({'res': 0})
    else:
        return JsonResponse({'res': 0})