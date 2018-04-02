import xadmin
from blog.models import blog,Tag,Category

class BlogAdmin(object):
    fields = ['blog_title', 'blog_content', 'category', 'tags', 'author', 'created_time', 'excerpt']
    search_fields = ['blog_content', 'blog_title', 'author']
    list_filter = ['created_time']

    list_display = (
        'blog_title',
        'author',
        'created_time',
        'modified_time'
    )
    class Media:
        js = ('/static/js/kindeditor/kindeditor-all-min.js',
              '/static/js/kindeditor/lang/zh-CN.js',
              '/static/js/kindeditor/config.js')


class TagAamin(object):
    fields = ['Tag_name']
    search_fields = ['Tag_name']
    list_filter = ['Tag_name']

class CategoryAamin(object):
    fields = ['Category_name']
    search_fields = ['Category_name']
    list_filter = ['Category_name']

xadmin.site.register(blog, BlogAdmin)
xadmin.site.register(Tag, TagAamin)
xadmin.site.register(Category, CategoryAamin)