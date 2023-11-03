from django import template
from django.db.models import Q

from menu.models import *
register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, main_menu):
    menu_items = MenuItem.objects.filter(name=main_menu)
    return {
        "menu_items": menu_items,
    }