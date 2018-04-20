"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views import static
from django.conf import settings
from upload_image import upload_image
from blog.feeds import AllPostsRssFeed
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
import xadmin
from blog.models import blog

info_dict = {
    'queryset': blog.objects.all(),
    'date_field': 'created_time',
}

urlpatterns = [
    url(r'^todolist/', include('todolist.urls', namespace='todolist')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^admin/', xadmin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^upload/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT, }),
    url(r'^xadmin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    url(r'^all/rss/$', AllPostsRssFeed(), name='rss'),
    url(r'^search/', include('haystack.urls')),
    url(r'^comment/', include('comments.urls'), name='comment'),
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'blog': GenericSitemap(info_dict)}},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^api/', include('api.urls'), name='api'),
]
