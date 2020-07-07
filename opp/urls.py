from django.shortcuts import render
from django.http import HttpResponse

from . import views
from django.urls import path,include

urlpatterns=[
    path("",views.index,name="index"),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.SignUp.as_view(), name='signup'),
    path('orgsignup/', views.OrganisationSignUp.as_view(), name='orgsignup'),
    path('userindex/', views.userindex.as_view(), name='userindex'),
    path('logout/', views.logout.as_view(), name='logout'),
    path('orgindex/', views.userindex.as_view(), name='orgindex'),
    path('addopportunity/', views.addOpportunity.as_view(), name='addOpportunity'),
]