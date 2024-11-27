from django.shortcuts import render

from django.http import HttpResponse

def iphone(request):
    return HttpResponse('<h1>IPHONE 16 NEW MOBILE WAS RELESED IN 2024 OCT</h1>')

def iphonepro(request):
    return HttpResponse('<h1>IPHONE 16 NEW MOBILE WAS RELESED IN 2024 dec</h1>')
# Create your views here.
