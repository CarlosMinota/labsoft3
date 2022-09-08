from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView, UpdateView
from django.contrib import messages

from .forms import ClienteForm
from .models import Producto, Cliente, Ciudad


#Se hace llamado al HTML que es la pagina inicial
class Home(TemplateView):
    template_name = 'index.html'

#Se hace llamado a la seccion de nosotros
class Nosotros(TemplateView):
    template_name = 'controlProyecto/nosotros.html'

#Se hace llamado a la seccion de promocion
class Promociones(TemplateView):
    template_name = 'controlProyecto/promocion.html'

#Se hace el registro del cliente
def crearCliente(request):
    ciudades = Ciudad.objects.all()
    cliente_errors = ""
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            messages.success(request, "!El registro ha sido exitoso!")
            return redirect('index')
        else:
            cliente_errors = cliente_form.errors
    else:
        cliente_form = ClienteForm()
    return render(request, 'controlProyecto/crear_cliente.html',{'cliente_form':cliente_form, 'ciudades':ciudades, 'cliente_errors':cliente_errors})

#Se hace la funcion para editar el perfil del cliente
def editarCliente(request, cedula):
    cliente_form = None
    error = None
    try:
        cliente = Cliente.objects.get(cedula = cedula)
        if request.method == "GET":
            cliente_form = ClienteForm(instance = cliente)
        else:
            cliente_form = ClienteForm(request.POST, instance = cliente)
            if cliente_form.is_valid():
                cliente_form.save()
            return redirect('index')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'controlProyecto/crear_cliente.html', {'cliente_form':cliente_form, 'error':error})

#se hace a funcion para eliminar el perfil del cliente de forma logica
def eliminarCliente(request, cedula):
    cliente = Cliente.objects.get(cedula = cedula)
    if request.method == 'POST':
        cliente.estado = False
        cliente.save()
        return redirect('index')
    return render(request, 'controlProyecto/eliminar_cliente.html', {'cliente':cliente})

#se hace la consuta para llamar a los productos que estan registrados en la base de datos
class ListaProductos(ListView):
    model = Producto
    template_name = 'controlProyecto/lista_productos.html'
    context_object_name = 'productos'
    queryset = Producto.objects.filter(estado = True)
