# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from comments.models import Comment
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@login_required(login_url="/blog/user_login")
def reply_comment(request, pk):
    if request.user.is_authenticated():
        reply_comment_username = request.user
    else:
        reply_comment_username = None

    if request.method == 'POST':
        reply_comment_content = request.POST.get('my-editormd-html-code', '')
        reply_comment_next = request.POST.get('next', 'value')
        if reply_comment_content is not None:
            find_comment = Comment.objects.get(id=pk)
            try:
                keep_comment = Comment.objects.create(name=reply_comment_username,
                                                  text=reply_comment_content,
                                                  parent=find_comment,
                                                  post=find_comment.post)
                keep_comment.save()
            except Exception, e:
                print e
        return HttpResponseRedirect(reply_comment_next)
    return HttpResponseRedirect('/blog')

@login_required(login_url="/blog/user_login")
@csrf_exempt
def remove_comment(request, pk):
    print request.path
    try:
        Comment.objects.get(id=pk).delete()
        return JsonResponse({'res': 1})
    except Exception, e:
        print e
        return JsonResponse({'res': 0})