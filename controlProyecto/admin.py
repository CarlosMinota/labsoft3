from django.contrib import admin

# Register your models here.

from .models import Question, Choise, Compra, Producto, Cliente, Envio, Carrito, Ciudad, Descuento, Departamento

admin.site.register(Question)
admin.site.register(Choise)
admin.site.register(Departamento)
admin.site.register(Ciudad)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(Envio)
admin.site.register(Carrito)
admin.site.register(Descuento)