# Generated by Django 3.2.7 on 2021-10-26 23:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technodevicesApp', '0006_alter_producto_fecha_publicacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='fecha_actualizacion',
            field=models.CharField(default=-5, max_length=10, verbose_name='Fecha actualización'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_publicacion',
            field=models.DateField(default=datetime.date.today, verbose_name='Fecha publicación'),
        ),
    ]
