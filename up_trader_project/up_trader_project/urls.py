from django.contrib import admin
from django.urls import include, path

from tree_menu.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tree_menu.urls', namespace='tree_menu')),
]

handler404 = page_not_found
