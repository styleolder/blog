# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from models import Comments
# Create your views here.
class Post_Comment(ListView):
    model = Comments
    template_name = 'Comment/index.html'
    context_object_name = 'Comments'