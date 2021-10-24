from django.conf    import settings
from django.db.models.query import QuerySet
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from technodevicesApp.models.producto import Producto
from technodevicesApp.serializers.productSerializer import ProductSerializer


class ProductDeleteView(generics.DestroyAPIView):
    serializer_class   = ProductSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Producto.objects.all()

    def delete(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().destroy(request, *args, **kwargs)