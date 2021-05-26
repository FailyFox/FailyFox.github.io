from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
from django.core.mail import send_mail


def index(request):
    customer = Articles.objects.all()
    return render(request, 'registration/index.html', {'customer': customer})


def registration(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('name')
            messages.success(request, 'Account was successfully created for ' + user)
            return redirect('success')
        else:
            error = "Форма не правильна"

    form = ArticlesForm

    data = {
        'form': form
    }
    return render(request, 'registration/Registration.html', data)


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            print('Success')
            return redirect('success')
        else:
            messages.warning(request, 'Wrong Email or Password')
            print('Wrong')

    form = ArticlesForm

    data = {
        'form': form
    }
    return render(request, 'registration/login.html', data)


def menu(request):
    return render(request, 'registration/Menu.html')


def success(request):
    return render(request, 'registration/success.html')


def constructor(request):
    return render(request, 'registration/Constructor_Pizza.html')


def about(request):
    return render(request, 'registration/about.html')


def anchous(request):
    return render(request, 'registration/pizza with anchous.html')


def conus(request):
    return render(request, 'registration/Pizza in conus form.html')


def close_pizza(request):
    return render(request, 'registration/Closed Pizza.html')


def fast_pizza(request):
    return render(request, 'registration/Fast pizza.html')


def fruit_pizza(request):
    return render(request, 'registration/Fruit Pizza.html')


def potato_pizza(request):
    return render(request, 'registration/Potato `s pizza.html')
