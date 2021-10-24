from rest_framework import serializers
from technodevicesApp.models.account import Account


class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [ 'telefono']

    def to_representation(self, obj):
        cuenta = Account.objects.get(id=obj.id)
        return {
            'telefono': cuenta.telefono,
            }
