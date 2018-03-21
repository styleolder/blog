from . import views
from django.conf.urls import url
app_name = 'comments'

urlpatterns = [
      url(r'^(?P<pk>[0-9]+)', views.Post_Comment,name='Post_Comment'),
]