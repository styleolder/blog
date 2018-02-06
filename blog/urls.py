from . import views
from django.conf.urls import url
app_name = 'blog'

urlpatterns = [
      url(r'^$', views.IndexView.as_view(),name='index'),
      url(r'^post/(?P<pk>[0-9]+)/$', views.PostView.as_view(),name='post'),
      url(r'^tags/(?P<id>\d+)', views.tags,name='tags'),
      url(r'^category/(?P<id>\d+)', views.category,name='category'),
      url(r'^login', views.login,name='login'),
      url(r'^logout', views.logout,name='logout'),
      url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
]