from . import views
from django.conf.urls import url
app_name = 'comments'

urlpatterns = [
      url(r'^reply/(?P<pk>[0-9]+)', views.reply_comment,name='reply_comment'),
      url(r'^remove/(?P<pk>[0-9]+)', views.remove_comment,name='remove_comment'),
]