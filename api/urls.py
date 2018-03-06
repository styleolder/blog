from . import views
from django.conf.urls import url
app_name = 'comments'

urlpatterns = [
     url(r'^blog_list/$', views.blog_list),
     url(r'^blog_detail/(?P<pk>[0-9]+)/$', views.blog_detail),
]