from django.db import models

# Create your models here.
class tablausuario(models.Model):
    usuario = models.CharField(max_length = 15)
    contra = models.CharField(max_length = 10)


class tablaproducto(models.Model):
    producto = models.CharField(max_length = 50)
    tipoproducto = models.CharField(max_length = 100)
    marcaproducto = models.CharField(max_length = 100)
    descripcionproducto = models.TextField(max_length = 100)
    stockproducto = models.IntegerField()
    precioproducto = models.DecimalField(max_digits=4, decimal_places=2)


class tablacompra(models.Model):
    cliente = models.CharField(max_length = 15)
    nombrecompra= models.CharField(max_length = 100)
    preciocompra = models.DecimalField(max_digits=4, decimal_places=2)
    cantidadcompra = models.IntegerField()
    preciototal = models.DecimalField(max_digits=4, decimal_places=2)
