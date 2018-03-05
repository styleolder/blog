from . import views
from django.conf.urls import url
app_name = 'comments'

urlpatterns = [
     url(r'^test/$', views.blog_list),
]