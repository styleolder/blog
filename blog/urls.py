from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
      url(r'^$', views.IndexView.as_view(),name='index'),
      url(r'^post/(?P<id>\d+)', views.post,name='post'),
      url(r'^tags/(?P<id>\d+)', views.tags,name='tags'),
      url(r'^category/(?P<id>\d+)', views.category,name='category'),
      url(r'^login', views.login,name='login'),
      url(r'^logout', views.logout,name='logout'),
]