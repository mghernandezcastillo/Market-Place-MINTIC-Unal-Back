from rest_framework import generics
from technodevicesApp.models.producto import Producto
from technodevicesApp.serializers.productSerializer import ProductSerializer

class ProductDetailView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset1 = Producto.objects.filter(pk = self.kwargs['pk'])
        return queryset1