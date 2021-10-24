from django.db import models
from .user import User
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    lastChangeDate = models.DateTimeField()
    isActive = models.BooleanField(default=True)
    email = models.EmailField('Email', max_length = 100, default = "", blank = '')
    telefono = models.CharField('Telefono', max_length= 15, default = "", blank = '')