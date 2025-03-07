from django import forms

class RoomSearchForm(forms.Form):
    ciudad = forms.CharField(
        label="Ciudad",
        max_length=100,
        required=False
    )
    tipo = forms.CharField(
        label="Tipo de Habitación",
        max_length=50,
        required=False
    )
    capacidad = forms.IntegerField(
        label="Capacidad Mínima",
        required=False
    )
    fecha_checkin = forms.DateField(
        label="Fecha de Check-In",
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    fecha_checkout = forms.DateField(
        label="Fecha de Check-Out",
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
