from django.urls import path
from presentfunc1.views import greeting, catalog, bikes

urlpatterns = [
    path('', greeting),
    path('catalog/', catalog),
    path('catalog/bikes/', bikes),
]
