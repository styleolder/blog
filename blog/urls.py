from . import views
from django.conf.urls import url
app_name = 'blog'
handler404 = "blog.views.page_not_found"

urlpatterns = [
      url(r'^$', views.IndexView.as_view(),name='index'),
      url(r'^post/(?P<pk>[0-9]+)/$', views.PostView.as_view(),name='post'),
      url(r'^category/(?P<pk>[0-9]+)', views.CategoryView.as_view(),name='category'),
      url(r'^login', views.login,name='login'),
      url(r'^logout', views.logout,name='logout'),
      url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
      url(r'^tags/(?P<pk>[0-9]+)', views.TagsView.as_view(),name='tags'),
      url(r'^user/(?P<pk>[0-9]+)', views.UserView.as_view(),name='user'),
]