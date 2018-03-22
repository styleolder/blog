# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/blog/user_login")
def sub_comment(request):
    pass

