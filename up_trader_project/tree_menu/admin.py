from django.contrib import admin

from tree_menu.models import Item, Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    Defines the interface of the "Menu" model in the admin panel.
    """
    list_display = ('name',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """
    Defines the interface of the "Item" model in the admin panel.
    """
    list_display = ('name', 'parent')
