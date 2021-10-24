from rest_framework import status, views
from rest_framework.response import Response
from technodevicesApp.serializers.categoriaSerializer import CategoriaSerializer


class CategoriaCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = CategoriaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)