from django.db import models
from .categoria import Categoria

# Create your models here.

class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length= 50)
    categoria = models.ForeignKey(Categoria, on_delete= models.PROTECT)

    def __str__(self):
        return self.nombre