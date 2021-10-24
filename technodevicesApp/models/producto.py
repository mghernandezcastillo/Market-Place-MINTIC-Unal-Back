from django.db import models
from .user import User
from .categoria import Categoria
from .marca import Marca
from datetime import date

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    vendedor = models.ForeignKey(User, related_name='vendedor', on_delete=models.CASCADE, null= True)
    titulo = models.CharField('Nombre', max_length= 50)
    marca = models.ForeignKey(Marca, on_delete= models.PROTECT)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    nuevo = models.BooleanField()
    categoria = models.ForeignKey(Categoria, related_name='categoria', on_delete= models.PROTECT)
    imagen1 = models.ImageField(upload_to = "imagenes", default = "", blank = '')
    imagen2 = models.ImageField(upload_to = "imagenes", default = "", blank = '')
    imagen3 = models.ImageField(upload_to = "imagenes", default = "", blank = '')
    fecha_publicacion = models.DateField('Fecha publicación', default=date.today)

    def __str__(self):
        return self.titulo
    


