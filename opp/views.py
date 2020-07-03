from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.conf import settings
import random

def index(request):
    return render(request,"index.html")