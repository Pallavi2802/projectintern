from django.shortcuts import render
from django.http import HttpResponse

from . import views
from django.urls import path,include

urlpatterns=[
    path("",views.index,name="index")
]