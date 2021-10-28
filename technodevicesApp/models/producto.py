from django.db import models
from django.conf import settings
from technodevicesApp.models.account import Account
from .user import User
from .categoria import Categoria
from .marca import Marca
from datetime import date

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    vendedor = models.CharField('vendedor', max_length= 50)
    titulo = models.CharField('Nombre', max_length= 50)
    marca = models.CharField("Marca", max_length= 50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    nuevo = models.BooleanField()
    categoria = models.ForeignKey(Categoria, related_name='categoria', on_delete= models.PROTECT)
    imagen1 = models.ImageField(upload_to = "imagenes", default = "", blank = '')
    imagen2 = models.ImageField(upload_to = "imagenes", default = "", blank = '')
    imagen3 = models.ImageField(upload_to = "imagenes", default = "", blank = '')
    email_contacto = models.EmailField('Email', max_length = 100, default = "", blank = '')
    fecha_publicacion = models.DateField('Fecha publicación', default=date.today)
    fecha_actualizacion = models.CharField('Fecha actualización', max_length= 10)

    def __str__(self):
        return self.titulo+str
    


