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
        items = Item.objects.select_related('parent', 'menu').filter(menu__title=menu).all()
        object = slug
        path = []
        while True:
            for obj in items:
                if object is None:
                    break
                if obj.title == object:
                    object = obj.parent.title
                    path.append(object)
                    break
            if object == menu:
                break
    else:
        items = None
    return {'parent': menu, 'button': menu, 'slug': slug, 'items': items}
