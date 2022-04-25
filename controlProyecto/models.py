import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('fecha de publicacion')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.choice_text

class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key= True)
    nombre_departamento = models.CharField(max_length= 30, blank= False, null= False)

    def __str__(self):
        return self.nombre_departamento

class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    nombre_ciudad = models.CharField(max_length=30, blank=False, null=False)
    departamento_id_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_ciudad

class Cliente(models.Model):
    id = models.AutoField(primary_key= True)
    cedula = models.CharField(max_length=  15, blank= False, null= False)
    nombreCliente = models.CharField(max_length= 100, blank= False, null= False)
    telefono = models.CharField(max_length= 10, blank= False, null= False)
    direccion = models.CharField(max_length= 40, blank= False, null= False)
    correo_electronico = models.CharField(max_length= 100, blank= False, null= False)
    ciudad_id_ciudad = models.ForeignKey(Ciudad, on_delete= models.CASCADE)

    def __str__(self):
        return self.nombreCliente

class Compra(models.Model):
    id_compra = models.AutoField(primary_key= True)
    precio = models.FloatField(blank= False, null= False)
    cliente_id_cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)

    def __str__(self):
        return str(self.id_compra)

class Envio(models.Model):
    STATUS_TYPE = (
        ('Despachando', 'Despachando'),
        ('Enviando', 'Enviando'),
        ('Entregado', 'Entregado'),
    )

    id_envio = models.AutoField(primary_key= True)
    estado_envio = models.CharField(max_length= 15, choices= STATUS_TYPE, blank= False, null= False)
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    compra_id_compra = models.ForeignKey(Compra, on_delete= models.CASCADE)

    def __str__(self):
        return str(self.estado_envio)

class Producto(models.Model):
    id_producto = models.AutoField(primary_key= True)
    nombre_producto = models.CharField(max_length= 100, blank= False, null= False)
    precio_producto = models.FloatField(blank= False, null= False)
    cantidad_disponible = models.IntegerField(blank= False, null= False)

    def __str__(self):
        return self.nombre_producto


class Descuento(models.Model):
    id_descuento = models.AutoField(primary_key= True)
    precio_descuento = models.FloatField(blank= False, null= False)
    estado_descuento = models.BooleanField('estado', default=True)
    producto_id_producto = models.ForeignKey(Producto, on_delete= models.CASCADE)

    def __str__(self):
        return str(self.estado_descuento)

class Carrito(models.Model):
    id_carrito = models.AutoField(primary_key= True)
    cantidad_carrito = models.IntegerField(blank= False, null= False)
    precio_carrito = models.FloatField(blank= False, null= False)
    producto_id_producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
    compra_id_compra = models.ForeignKey(Compra, on_delete= models.CASCADE)

    def __str__(self):
        return str(self.precio_carrito)