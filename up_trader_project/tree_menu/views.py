from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from tree_menu.models import Item


def index(request: WSGIRequest, *args, **kwargs) -> HttpResponse:
    """
    Обрабатывает запрос к главной странице, в том числе по слагу. Делает
    Запрос к базе данных для отправки и отображения пользователю возможных
    меню. Данный запрос, ответственным за отрисовку пунктов меню, не посчитал,
    так как в реальности пользователь изначально должен видеть какие варианты
    различных меню можно нажать. Но при необходимости, могу обойтись без
    данного запроса. Либо название меню захардкодить в шаблоне `index` при
    вызове тега `draw_menu` или можно непосредственно в теге `draw_menu`
    перебрать в цикле `queryset` и поместить в массив названия объектов,
    которые не имеют родителя. При необходимости могу переделать.
    Менюшки и текущий слаг передаются в шаблон.
    """
    template = 'tree_menu/index.html'
    menus = Item.objects.filter(is_menu=True).all()
    current_slug = kwargs.get('slug')
    context = {'menus': menus, 'slug': current_slug}
    return render(request, template, context)
