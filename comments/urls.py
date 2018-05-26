from . import views
from django.conf.urls import url
app_name = 'comments'

urlpatterns = [
      url(r'^post/(?P<pk>[0-9]+)',views.Post_Comment.as_view(),name='post_comment')
]