from django import template

from items.models import Category

register = template.Library()


@register.simple_tag()
def tags_categories():
    return Category.objects.all()
