# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from api import serializers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', serializers.UserViewSet)
router.register(r'blogs', serializers.BlogViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include_docs_urls()),
]