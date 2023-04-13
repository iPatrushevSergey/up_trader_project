from django.urls import path

from tree_menu.views import index


app_name = 'tree_menu'

urlpatterns = [
    path('', index, name='main'),
    path('<slug:slug>/', index, name='slug'),
]
