from django.urls import path
from presentfunc3.views import reviews, aboutbike, socnet

urlpatterns = [
    path('reviews/', reviews),
    path('catalog/bike/suzuki/', aboutbike),
    path('socnet/', socnet),
]