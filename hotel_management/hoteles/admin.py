from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Hotel, Habitacion, Usuario, Reservacion

admin.site.register(Hotel)
admin.site.register(Habitacion)
admin.site.register(Usuario)
admin.site.register(Reservacion)
