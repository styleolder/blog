from django import template
from ..models import blog, Category, Tag
register = template.Library()
from django.utils.safestring import mark_safe
import markdown

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

@register.simple_tag
def archives():
    return blog.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_tags():
    return Tag.objects.all()

@register.simple_tag
def get_Category():
    return Category.objects.all().order_by("pk")

@register.simple_tag
def get_toc():
    tocs = blog.objects.all().order_by("-pk")
    return tocs

