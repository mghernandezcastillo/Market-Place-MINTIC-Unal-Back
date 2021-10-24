from rest_framework import serializers
from technodevicesApp.models.account import Account


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [ 'email']

    def to_representation(self, obj):
        cuenta = Account.objects.get(id=obj.id)
        return {
            'email': cuenta.email,
            }
