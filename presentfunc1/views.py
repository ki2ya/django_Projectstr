from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def greeting(request):
    return HttpResponse("Hello, Mentors")


def catalog(request):
    return HttpResponse("catalog")

def bikes(request):
    return HttpResponse("suzuki")
