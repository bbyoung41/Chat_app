from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, aauthenticate


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password_a = request.POST.get('name')
        user = authenticate(username=name, password=password_a)
        if user is not None:
            #return render(request, 'home.html')
            return HttpResponse('login success')
        else:
            return HttpResponse('Login not success')
    else:
        return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(name, email, password)
        user.save()
        return HttpResponse(f"success")
    else:
        return render(request, 'registration/sign up.html')
