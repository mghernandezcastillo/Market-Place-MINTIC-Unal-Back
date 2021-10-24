from rest_framework import serializers
from technodevicesApp.models.productimages import ProductImages


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['imagen', 'producto']

    def to_representation(self, obj):
        Productimage = ProductImages.objects.get(id=obj.id)
        return {
            'nombre': Productimage.imagen,
            'producto': Productimage.producto
            }