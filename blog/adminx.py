import xadmin
from blog.models import blog

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

xadmin.site.register(blog, BlogAdmin)