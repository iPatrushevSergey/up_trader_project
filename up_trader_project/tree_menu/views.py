from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls.exceptions import Resolver404

from tree_menu.models import Item


def index(request: WSGIRequest, *args, **kwargs) -> HttpResponse:
    template = 'tree_menu/index.html'
    menus = Item.objects.filter(is_menu=True).all()
    slug = kwargs.get('slug')
    context = {'menus': menus, 'slug': slug}
    return render(request, template, context)


def page_not_found(
        request: WSGIRequest,
        exception: Resolver404,
) -> HttpResponseNotFound:
    pass
