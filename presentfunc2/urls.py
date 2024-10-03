from django.urls import path
from presentfunc2.views import index, about, contact

urlpatterns = [
    path('general/', index),
    path('about/', about),
    path('contacts/', contact),
]