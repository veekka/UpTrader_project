from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class MenuItem(MPTTModel):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('menu_item', kwargs={'menu_slug': self.slug})


    class Meta:
        verbose_name = 'Пункт категории меню'
        verbose_name_plural = 'Пункты категорий меню'