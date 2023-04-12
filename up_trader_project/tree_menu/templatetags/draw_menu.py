from django import template

from tree_menu.models import Menu


register = template.Library()


@register.inclusion_tag('tree_menu/template_tags/test.html')
def show_test_menu():
    menus = Menu.objects.all()
    return {'menus': menus}
