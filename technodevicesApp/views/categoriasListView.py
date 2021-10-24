from rest_framework import generics
from technodevicesApp.models.categoria import Categoria
from technodevicesApp.serializers.categoriaSerializer import CategoriaSerializer

class CategoriasListView(generics.ListAPIView):
    serializer_class   = CategoriaSerializer

    def get_queryset(self):
        queryset1 = Categoria.objects.all()
        return queryset1