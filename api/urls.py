# -*- coding: utf-8 -*-
from api import views
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from todolist.models import User
from rest_framework.documentation import include_docs_urls

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff', 'user_icon')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include_docs_urls(title="blogs")),
    url(r'^Blog/$', views.BlogList.as_view())
]