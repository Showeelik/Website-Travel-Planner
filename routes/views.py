from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Route
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
    """
    Страница с деталями маршрута.
    """
    route = get_object_or_404(Route, pk=pk, user=request.user)
    return render(request, 'routes/route_detail.html', {'route': route})