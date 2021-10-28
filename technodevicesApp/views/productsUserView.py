'''from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from technodevicesApp.models.producto import Producto
from technodevicesApp.serializers.productSerializer import ProductSerializer

class ProductsUserDetailView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print("request:", self.request)
        print("Args:", self.args)
        print("KWArgs:", self.args)
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != self.kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Producto.objects.filter(vendedor_id = self.request.user)
        return queryset'''

from django.db.models import query
from rest_framework import status, views, generics
from rest_framework.response import Response
from technodevicesApp.serializers.productSerializer import ProductSerializer
from django.conf import settings
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from technodevicesApp.models.producto import Producto
from technodevicesApp.serializers.productSerializer import ProductSerializer
from technodevicesApp.models.account import Account


class ProductsUserView(generics.ListAPIView):
    serializer_class   = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

    
        account = Account.objects.get(user_id= self.kwargs['user'])
        vendedor_id = account.user_id
        vendedor_nombre = account.name
        
        
        queryset = Producto.objects.filter(vendedor=vendedor_nombre+"-"+str(vendedor_id))
        return queryset