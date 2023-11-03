from django.urls import path, re_path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name="menu/home.html")),
    path('menu/<slug:menu_slug>/', menu_item, name='menu_item'),
]