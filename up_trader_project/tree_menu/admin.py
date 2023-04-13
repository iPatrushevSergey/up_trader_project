from django.contrib import admin

from tree_menu.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """
    Defines the interface of the "Item" model in the admin panel.
    """
    list_display = ('title', 'parent', 'menu')
    prepopulated_fields = {'slug': ('title',)}
