from django.db import models
from .user import User
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    lastChangeDate = models.DateTimeField()
    isActive = models.BooleanField(default=True)
    telefono = models.CharField('Telefono', max_length= 15, default = "", blank = '')
    name = models.CharField('Name', max_length = 30)


    def __str__(self):
        return self.name