from rest_framework import generics
from technodevicesApp.models.account import Account
from technodevicesApp.serializers.accountSerializer import AccountSerializer

class ContactDetailsView(generics.ListAPIView):
    serializer_class = AccountSerializer

    def get_queryset(self):
        queryset1 = Account.objects.filter(pk = self.kwargs['pk'])
        return queryset1