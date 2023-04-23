from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from users.utils import get_user_from_request
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'GET':
        data = {
            'form': LoginForm,
            'user': get_user_from_request(request)
        }

        return render(request, template_name='users/login.html', context=data)

    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('/')
            else:
                form.add_error('username', 'Неверный логин или пароль')

        data = {
            'form': form,
            'user': get_user_from_request(request)
        }

        return render(request, template_name='users/login.html', context=data)


def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    if request.method == 'GET':
        data = {
            'form': RegisterForm,
            'user': get_user_from_request(request)
        }

        return render(request, template_name='users/register.html', context=data)

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            if form.cleaned_data.get('password_1') == form.cleaned_data.get('password_2'):
                user = User.objects.create_user(
                    username = form.cleaned_data.get('username'),
                    password = form.cleaned_data.get('password_1')
                )

                login(request, user)
                return redirect('/')

            else:
                form.add_error('password_1', 'Пароли не совпадают!')

        data = {
            'form': form,
            'user': get_user_from_request(request)
        }

        return render(request, 'users/register.html', context=data)

