from django.db import models

# Create your models here.
from django.db import models

class Hotel(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Habitacion(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='habitaciones')
    tipo = models.CharField(max_length=50)  # Ej: standard, premium, vip
    capacidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hotel.nombre} - {self.tipo}"


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Reservacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reservaciones')
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, related_name='reservaciones')
    fecha_checkin = models.DateTimeField()
    fecha_checkout = models.DateTimeField()
    estado = models.CharField(max_length=50, default='confirmada')
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reserva {self.id} - {self.usuario.nombre}"
