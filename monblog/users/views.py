from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    
    return render(request, 'users/signup.html', {'form': SignUpForm})


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username_form = form.cleaned_data['username']
            password_form = form.cleaned_data['password']
            user = authenticate(request, username=username_form, password=password_form)

            if user:
                login(request, user)
            else:
                return HttpResponse("Connexion impossible")
            return redirect('article_list')
        
    return render(request, 'users/signin.html', {'form' : SignInForm})




def log_out(request):
    logout(request)
    return redirect('article_list')