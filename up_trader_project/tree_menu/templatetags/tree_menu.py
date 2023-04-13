from django import template

from tree_menu.models import Item
from tree_menu.utils import query_debugger


register = template.Library()


@register.inclusion_tag(
        'tree_menu/template_tags/menu.html',
        takes_context=True,
)
@query_debugger
def draw_menu(context, menu):
    slug = context.get('slug')
    if slug:
        items = Item.objects.select_related('menu', 'parent').filter(menu__title=menu).all()
    else:
        items = None
    return {'menu': menu, 'slug': slug, 'items': items}
