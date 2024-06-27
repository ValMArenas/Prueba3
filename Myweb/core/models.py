from django.db import models
from distutils.command.upload import upload

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id Categoria') 
    nombreCategoria= models.CharField(max_length=40, verbose_name='Nombre Categoria')

    def __str__(self):
        return self.nombreCategoria


class Planta(models.Model):
    idPlanta = models.CharField(primary_key=True, max_length=5, verbose_name='id Planta')
    imagen= models.ImageField(upload_to="imagenes", null=True, verbose_name='imagen')
    nombre = models.CharField(max_length=40, verbose_name='nombre')
    categoria= models.ForeignKey('categoria', on_delete=models.CASCADE, verbose_name='categoria')
    stock= models.IntegerField(verbose_name='ctock')
    precio= models.IntegerField(verbose_name='precio')

    def __str__(self):
        return self.idPlanta
    
class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
  
    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Planta', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)