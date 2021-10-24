from django.contrib import admin

from .models.account import Account
from .models.user import User
from .models.producto import Producto
from .models.categoria import Categoria
from .models.marca import Marca
from .models.productimages import ProductImages


admin.site.register(User)
admin.site.register(Account)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(ProductImages)

# Register your models here.
