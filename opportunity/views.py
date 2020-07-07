from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.conf import settings
import random
from django.core.validators import validate_email
from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework.views import APIView
from opp.models import UserProfile


class Login(APIView):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)

            try:
                users = UserProfile.objects.get(user=user)

                if users.is_Organisation:
                     return render(request,'orgindex.html')
                else:
                    return render(request,'userindex.html')

            except:
                return render(request, 'login.html')


class SignUp(APIView):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        if request.POST['password'] == request.POST['cnfpassword']:

            try:
                validate_email(request.POST['email'])
            except:
                return render(request, 'signup.html', {"error": "Valid email Id please"})
            try:
                email = UserProfile.objects.get(request.POST['email'])
                return render(request, 'signup.html', {"error": "Account already exists"})
            except:
                pass
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username already exists'})
            except:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                userprofile = UserProfile(user=user, email=request.POST['email'], name=request.POST['name'],
                                          is_Organisation=False)
                user.email = request.POST['email']
                user.save()
                userprofile.save()
                return redirect('login')


class OrganisationSignUp(APIView):
    def get(self, request):
        return render(request, 'orgsignup.html')

    def post(self, request):
        if request.POST['password'] == request.POST['cnfpassword']:

            try:
                validate_email(request.POST['email'])
            except:
                return render(request, 'orgsignup.html', {"error": "Valid email Id please"})
            try:
                email = UserProfile.objects.get(request.POST['email'])
                return render(request, 'orgsignup.html', {"error": "Account already exists"})
            except:
                pass
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'orgsignup.html', {'error': 'Username already exists'})
            except:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                userprofile = UserProfile(user=user, email=request.POST['email'], name=request.POST['name'],
                                          is_Organisation=True)
                user.email = request.POST['email']
                user.save()
                userprofile.save()
                return redirect('login')




class userindex(APIView):
    def get(self, request):
        return render(request, 'userindex.html')

class logout(APIView):
    def get(self, request):
        auth.logout(request)
        return redirect('index')

class orgindex(APIView):
    def get(self, request):
        return render(request, 'orgindex.html')