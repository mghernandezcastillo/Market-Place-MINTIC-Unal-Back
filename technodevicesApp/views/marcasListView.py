from rest_framework import generics
from technodevicesApp.models.marca import Marca
from technodevicesApp.serializers.marcaSerializer import MarcaSerializer

class MarcasListView(generics.ListAPIView):
    serializer_class   = MarcaSerializer

    def get_queryset(self):
        queryset1 = Marca.objects.all()
        return queryset1