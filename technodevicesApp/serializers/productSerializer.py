from rest_framework import serializers
from technodevicesApp.models.producto import Producto
from drf_extra_fields.fields import Base64ImageField
class ProductSerializer(serializers.ModelSerializer):

    imagen1 = Base64ImageField(required=False)
    '''
    imagen2 = Base64ImageField(required=False)
    imagen3 = Base64ImageField(required=False)
    '''
    vendedor = serializers.StringRelatedField()

    ''' agregar imagenes a los fields '''

    class Meta:
        model = Producto   #modelo que se va a usar
        fields = ['id','titulo','marca','precio','descripcion','nuevo','categoria', 'vendedor','imagen1', 'fecha_publicacion']  #claves que se quieren usar, adicional la cuenta, para conocer los datos de la cuenta asosciada a ese usario
 
    '''def create(self, validated_data): #validated_data: datos que ya han sido previamente validados,
        productInstance = Producto.objects.create(**validated_data) # crea el usuario con las claves seleccionadas sin la clave account y le asigna el id de ese usuario creado a la variable
        ProductImages.objects.create(producto=productInstance) # crea la cuenta con el id del usuario creado y los datos de la cuenta
        return productInstance'''


