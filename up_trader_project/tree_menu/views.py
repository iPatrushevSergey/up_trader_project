from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls.exceptions import Resolver404


def index(request: WSGIRequest) -> HttpResponse:
    template = 'tree_menu/index.html'
    context = {'text': 'Tree menu home page'}
    return render(request, template, context)


def page_not_found(
        request: WSGIRequest,
        exception: Resolver404,
) -> HttpResponseNotFound:
    pass
