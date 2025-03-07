from django.shortcuts import render
from django.db.models import Q
from .models import Habitacion
from .forms import RoomSearchForm

def search_rooms(request):
    form = RoomSearchForm(request.GET or None)
    habitaciones = Habitacion.objects.all()

    if form.is_valid():
        ciudad = form.cleaned_data.get('ciudad')
        tipo = form.cleaned_data.get('tipo')
        capacidad = form.cleaned_data.get('capacidad')
        fecha_checkin = form.cleaned_data.get('fecha_checkin')
        fecha_checkout = form.cleaned_data.get('fecha_checkout')

        # Filtro por ciudad (case-insensitive).
        if ciudad:
            habitaciones = habitaciones.filter(hotel_ciudad_icontains=ciudad)
        
        # Filtro por tipo de habitación (case-insensitive).
        if tipo:
            habitaciones = habitaciones.filter(tipo__icontains=tipo)
        
        # Filtro por capacidad mínima.
        if capacidad:
            habitaciones = habitaciones.filter(capacidad__gte=capacidad)
        
        # Excluir habitaciones que tengan reservaciones en las fechas indicadas
        # (ejemplo simple: si hay cruce con [fecha_checkin, fecha_checkout], se excluye).
        if fecha_checkin and fecha_checkout:
            # Excluimos habitaciones que tienen reservaciones que se solapen con el rango
            habitaciones = habitaciones.exclude(
                reservaciones_fecha_checkin_lt=fecha_checkout,
                reservaciones_fecha_checkout_gt=fecha_checkin
            )

    context = {
        'form': form,
        'habitaciones': habitaciones
    }
    return render(request, 'hoteles/search_rooms.html', context)