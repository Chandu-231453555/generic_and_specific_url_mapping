from django.shortcuts import render

from django.http import HttpResponse

def samsung(request):
    return HttpResponse('<h1>samsung 17 was relesed in 2024</h1>')
def samsungpro(request):
    return HttpResponse('<h1>samsung 17 pro released in 2025 jan 28</h1>')


# Create your views here.
