import xadmin
from comments.models import Comment

class CommentAdmin(object):
    fields = ['parent', 'text', 'post', 'name']
    list_filter = ['created_time']
    list_display = (
        'id',
        'name',
        'created_time',
        'parent',
    )

xadmin.site.register(Comment, CommentAdmin)