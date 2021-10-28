from rest_framework import serializers
from technodevicesApp.models.marca import Marca


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = [ 'nombre','categoria']

    def to_representation(self, obj):
        marca = Marca.objects.get(id=obj.id)
        return {
            'nombre': marca.nombre,
            'categoria': marca.categoria_id
            }