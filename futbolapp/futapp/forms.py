from django import forms
from django.contrib.auth.models import User
from .models import Jugador
from .models import Profesor
from .models import Pago

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
 
class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['jugador', 'equipo', 'tipo_pago', 'monto', 'fecha_pago', 'mes']

    def clean(self):
        cleaned_data = super().clean()
        tipo_pago = cleaned_data.get("tipo_pago")
        mes = cleaned_data.get("mes")

        if tipo_pago == 'M' and not mes:
            self.add_error('mes', 'Debe seleccionar el mes para el pago de la mensualidad.')


