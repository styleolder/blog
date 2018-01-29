from django import template
from ..models import blog, Category, Tag

register = template.Library()

@register.simple_tag
def archives():
    return blog.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_tags():
    return Tag.objects.all()

@register.simple_tag
def get_Category():
    return Category.objects.all().order_by("pk")