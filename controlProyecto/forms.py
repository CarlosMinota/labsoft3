from django import forms
from .models import Cliente

#formulario del cliente
class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['cedula', 'nombre_cliente', 'telefono', 'direccion', 'correo_electronico', 'ciudad']
        labels = {
            'cedula': 'Cedula',
            'nombre_cliente': 'Nombre',
            'telefono': 'Telefono',
            'direccion': 'Dirección',
            'correo_electronico': 'Correo electronico',
            'ciudad': 'Ciudad'
        }
        widgets = {
            'cedula': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su cedula',
                    'id': 'cedula'
                }
            ),
            'nombre_cliente': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                    'id': 'nombre'
                }
            ),
            'telefono': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su telefono',
                    'id': 'telefono'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su dirección',
                    'id': 'direccion'
                }
            ),
            'correo_electronico': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su email',
                    'id': 'email'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-control',
                    'choises': 'Seleccione su ciudad',
                    'id': 'ciudad'
                }
            )
        }