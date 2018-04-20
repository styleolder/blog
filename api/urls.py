from . import views
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from todolist.models import User
from blog.models import blog


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = blog
        fields = ('id', 'blog_title', 'blog_content', 'created_time','modified_time','category','tags','author','excerpt')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = BlogSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^blog_list/$', views.BlogList)
]