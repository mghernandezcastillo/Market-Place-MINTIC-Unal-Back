from rest_framework import generics
from technodevicesApp.models.producto import Producto
from technodevicesApp.serializers.productSerializer import ProductSerializer

class AllProductsListView(generics.ListAPIView):
    serializer_class   = ProductSerializer

    def get_queryset(self):
        queryset1 = Producto.objects.all()
        return queryset1