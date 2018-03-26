import xadmin
from todolist.models import TodoList

class TodoListAdmin(object):
    fields = ('todolist_state', 'todolist_text','pub_date','dodolist_flag')
    list_filter = ['pub_date']
    search_fields = ['todolist_text']
    list_display = ('todolist_text', 'pub_date', 'todolist_state', 'dodolist_flag')
    list_display_links = ('todolist_text', 'pub_date')
    list_editable = ('todolist_state', 'dodolist_flag')

xadmin.site.register(TodoList, TodoListAdmin)