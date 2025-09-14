from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request, 'home.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
