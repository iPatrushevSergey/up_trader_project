from typing import Union

from django import template
from django.db.models import QuerySet
from django.template.context import RequestContext

from tree_menu.models import Item
from tree_menu.utils import query_debugger


register = template.Library()


@register.inclusion_tag(
        'tree_menu/template_tags/menu.html',
        takes_context=True,
)
@query_debugger
def draw_menu(context: RequestContext, menu: str
              ) -> dict[str, Union[QuerySet, str, list[str]]]:
    """
    Функция-тег для отрисовки пунктов меню. Выполняет один запрос к БД.
    Операция перебора `queryset` в словаре и доступ к атрибутам объектов
    запросов к БД не требуют (ни в функции, ни в шаблонах).
    Из контекста извлекается текущий слаг. Для возможности прохода
    по определнному пути заводится и наполняется родителями текущего слага
    динамический массив `path_to_slug`. В шаблон отправляются: `queryset`
    пунктов меню, текущий слаг, родитель - название меню, выбранное и нажатое
    пользователем меню, а также путь - нажатые пункты от меню до текущего
    слага.
    """
    current_slug = context.get('slug')
    path_to_slug = []
    if current_slug:
        items = Item.objects.select_related(
            'parent', 'menu'
        ).filter(menu__title=menu).all()
        path_to_slug.append(current_slug)
        step = current_slug
        while True:
            for item in items:
                if item.title == step:
                    step = item.parent.title
                    path_to_slug.append(step)
                    break
                if step == menu:
                    break
            if step == menu:
                break
    else:
        items = None
    return {
        'items': items,
        'slug': current_slug,
        'parent': menu,
        'button': menu,
        'path': path_to_slug
    }
