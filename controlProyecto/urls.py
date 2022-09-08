from django.urls import path
from .views import crearCliente, ListaProductos, editarCliente, eliminarCliente, Nosotros, Promociones

urlpatterns = [
    path('crear-cliente/', crearCliente, name='crearCliente'),
    path('productos/', ListaProductos.as_view(), name='productos'),
    path('editar-cliente/<slug:cedula>', editarCliente, name='editarCliente'),
    path('eliminar-cliente/<slug:cedula>', eliminarCliente, name='eliminarCliente'),
    path('nosotros/', Nosotros.as_view(), name='nosotros'),
    path('promociones/', Promociones.as_view(), name='promocion'),
]
