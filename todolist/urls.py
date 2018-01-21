from django.conf.urls import url

from . import views
app_name = 'todolist'

urlpatterns = [
      url(r'^$', views.index,name='index'),
      url(r'^user', views.user,name='user'),
      url(r'^status', views.status,name='status'),
      url(r'^login', views.login,name='login'),
      url(r'^zone', views.zone,name='zone'),
      url(r'^logout', views.logout,name='logout')
]