from django.shortcuts import render

from django.http import HttpResponse

def vivo(request):
    return HttpResponse('<h1>vivo 15 was relesed in 2024</h1>')
def vivopro(request):
    return HttpResponse('<h1>vivo 16 pro released in 2025 jan 28</h1>')


# Create your views here.
