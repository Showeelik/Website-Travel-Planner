from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически авторизуем пользователя
            return redirect(reverse('home'))  # Перенаправляем на главную страницу
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    """
    Главная страница.
    """
    context = {
        'user': request.user if request.user.is_authenticated else None,
    }
    return render(request, 'home.html', context)