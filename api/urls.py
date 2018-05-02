# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from api import serializers
from rest_framework_jwt.views import obtain_jwt_token


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', serializers.UserViewSet, base_name="users")
router.register(r'blogs', serializers.BlogViewSet, base_name="blogs")
router.register(r'codes', serializers.SmsCodeViewSet, base_name="codes")


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include_docs_urls()),
    url(r'^api-token-auth/', obtain_jwt_token),
]