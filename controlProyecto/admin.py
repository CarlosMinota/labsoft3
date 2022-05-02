from django.contrib import admin

# Register your models here.

from .models import Question, Choise, Compra, Producto, Cliente, Envio, Carrito, Ciudad, Descuento, Departamento

admin.site.register(Question)
admin.site.register(Choise)
admin.site.register(Envio)