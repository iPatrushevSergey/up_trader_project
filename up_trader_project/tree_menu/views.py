from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls.exceptions import Resolver404

from tree_menu.models import Menu


def index(request: WSGIRequest, *args, **kwargs) -> HttpResponse:
    template = 'tree_menu/index.html'
    menus = Menu.objects.all()
    context = {'menus': menus, 'slug': kwargs.get('slug')}
    return render(request, template, context)


def page_not_found(
        request: WSGIRequest,
        exception: Resolver404,
) -> HttpResponseNotFound:
    pass
