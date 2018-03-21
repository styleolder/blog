from . import views
from django.conf.urls import url
app_name = 'comments'

urlpatterns = [
      url(r'^(?P<pk>[0-9]+)', views.sub_comment,name='sub_comment'),
]