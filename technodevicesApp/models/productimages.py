from django.db import models
from technodevicesApp.models.producto import Producto

# Create your models here.

class ProductImages(models.Model):
    imagen = models.ImageField(upload_to = "imagenes", null = True, default = "imagenes/default-product-image", blank = '')
    producto = models.ForeignKey(Producto, related_name='producto', on_delete=models.CASCADE)