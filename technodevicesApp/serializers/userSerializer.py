from rest_framework import serializers
from technodevicesApp.models.user import User
from technodevicesApp.models.account import Account
from technodevicesApp.serializers.accountSerializer import AccountSerializer
class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User   #modelo que se va a usar
        fields = ['id', 'username', 'password', 'name', 'account']  #claves que se quieren usar, adicional la cuenta, para conocer los datos de la cuenta asosciada a ese usario
 
    def create(self, validated_data): #validated_data: datos que ya han sido previamente validada,
        accountData = validated_data.pop('account') # trae los datos de la cuenta los asigna a la variable, y se borra de validated_data
        userInstance = User.objects.create(**validated_data) # crea el usuario con las claves seleccionadas sin la clave account y le asigna el id de ese usuario creado a la variable
        Account.objects.create(user=userInstance, **accountData) # crea la cuenta con el id del usuario creado y los datos de la cuenta
        return userInstance
 
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'account': {
                'user': account.user_id,
                'id': account.id,
                'lastChangeDate': account.lastChangeDate,
                'isActive': account.isActive,
                'email': account.email,
                'telefono': account.telefono
            }
        }