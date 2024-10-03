
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def reviews(request):
    return HttpResponse("Здеcь должны быть отзывы")


def aboutbike(request):
    return HttpResponse("Хороший аппарат")


def socnet(request):
    return HttpResponse("Social Networks")
# Create your views here.
