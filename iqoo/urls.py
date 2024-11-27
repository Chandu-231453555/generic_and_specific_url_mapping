from django.urls import path
from iqoo.views import *

urlpatterns=[
    path('iqoo/',iqoo,name='iqoo'),
    path('iqoopro/',iqoopro,name='iqoopro'),
]