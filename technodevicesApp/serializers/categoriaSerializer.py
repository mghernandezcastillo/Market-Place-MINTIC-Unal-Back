from rest_framework import serializers
from technodevicesApp.models.categoria import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre']
    def to_representation(self, obj):
        categoria = Categoria.objects.get(nombre=obj.nombre)
        return {
            'nombre': categoria.nombre
            }