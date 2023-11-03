from django.shortcuts import render, get_object_or_404

from menu.models import MenuItem

def menu_item(request, menu_slug):
    menu_item = get_object_or_404(MenuItem, slug=menu_slug)
    context = {
        'menu_item': menu_item,
    }
    return render(request, 'menu/menu_item.html', context=context)
