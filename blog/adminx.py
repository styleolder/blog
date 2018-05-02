import xadmin
from blog.models import blog,Tag,Category,ShortMessage


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

class ShortMessageAamin(object):
    fields = ['ShortMessage_mobile','ShortMessage_code','ShortMessage_message','ShortMessage_type','ShortMessage_created_time']
    list_filter = ['ShortMessage_created_time']
    search_fields = ['ShortMessage_mobile']
    list_display = (
       'ShortMessage_mobile',
       'ShortMessage_code',
       'ShortMessage_type',
       'ShortMessage_created_time'
    )
xadmin.site.register(blog, BlogAdmin)
xadmin.site.register(Tag, TagAamin)
xadmin.site.register(ShortMessage, ShortMessageAamin)
xadmin.site.register(Category, CategoryAamin)