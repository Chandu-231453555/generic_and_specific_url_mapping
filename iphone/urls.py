from django.urls import path
from iphone.views import *

urlpatterns=[
    path('iphone/',iphone,name='iphone'),
    path('iphonepro/',iphonepro,name='iphonepro'),
]