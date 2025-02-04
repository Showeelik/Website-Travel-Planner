from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Route
from reviews.forms import ReviewForm
from .forms import RouteForm

@login_required
def route_list(request):
    """
    Страница со списком маршрутов пользователя.
    """
    routes = Route.objects.filter(user=request.user)
    return render(request, 'routes/route_list.html', {'routes': routes})

@login_required
def route_create(request):
    """
    Страница для создания нового маршрута.
    """
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            route = form.save(commit=False)
            route.user = request.user
            route.save()
            
            return redirect('route_list')
    else:
        form = RouteForm()

    return render(request, 'routes/route_form.html', {'form': form})


@login_required
def route_detail(request, pk):
    route = get_object_or_404(Route, pk=pk, user=request.user)
    reviews = route.reviews.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.route = route
            try:
                review.save()
                
                # Отправляем уведомление владельцу маршрута
                if route.user != request.user:
                    send_notification.delay(route.user.id, f"Новый отзыв на ваш маршрут: {route.title}")
                
                messages.success(request, "Отзыв успешно добавлен!")
                return redirect('route_detail', pk=pk)
            except IntegrityError:
                messages.error(request, "Вы уже оставили отзыв на этот маршрут.")
    else:
        form = ReviewForm()

    return render(request, 'routes/route_detail.html', {'route': route, 'reviews': reviews, 'form': form})