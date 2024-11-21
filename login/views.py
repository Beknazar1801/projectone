from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseNotAllowed
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse


# Create your views here.

class Loginclass(TemplateView):
    template_name = 'pages/login.html'
    success_url = 'pages/home.html'

class Logoutclass(TemplateView):
    template_name = 'pages/logout.html'

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт {username} успешно создан! Теперь вы можете войти.')
            return redirect('login')  # Убедитесь, что у вас есть соответствующий URL для логина
    else:
        form = UserRegistrationForm()
    return render(request, 'pages/register.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('order_success'))
    return HttpResponseNotAllowed(['POST'])

def order_success(request):
    return render(request, 'pages/order_success.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Переход на домашнюю страницу после входа
        else:
            return HttpResponse("Неверный логин или пароль", status=400)
    else:
        return render(request, 'pages/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('home')