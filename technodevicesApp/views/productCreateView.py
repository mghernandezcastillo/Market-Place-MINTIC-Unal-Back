from rest_framework import status, views
from rest_framework.response import Response
from technodevicesApp.models.producto import Producto
from technodevicesApp.serializers.productSerializer import ProductSerializer
from django.conf import settings
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from technodevicesApp.models.user import User
from technodevicesApp.models.account import Account
from technodevicesApp.serializers.userSerializer import UserSerializer


class ProductCreateView(views.APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data

       
            archivo1 = validated_data['imagen1']
            archivo1.name = 'mi_foto1.png'
            validated_data['imagen1'] = archivo1
            '''  
            archivo2 = validated_data['imagen2']
            archivo2.name = 'mi_foto2.png'
            validated_data['imagen2'] = archivo2

            archivo3 = validated_data['imagen3']
            archivo3.name = 'mi_foto3.png'
            validated_data['imagen3'] = archivo3
            '''

            account = Account.objects.get(user_id= kwargs['pk'])
            telefono = account.telefono
            email = account.email

            

            producto = Producto(vendedor = self.request.user, **validated_data)
            producto.save()
            serializer_response = ProductSerializer(producto)  

            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)