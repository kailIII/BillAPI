# viewsets.py
from client.models import catKindClient, catClient, catBusinessContact
from client.serializers import KindClientSerializer, ClientSerializer, BusinessContactSerializer 
from rest_framework import viewsets
 
 #class
 
class KindClientViewSet(viewsets.ModelViewSet):
    
    serializer_class = KindClientSerializer
    queryset = catKindClient.objects.all()
    
class ClientViewSet(viewsets.ModelViewSet):
    
    serializer_class = ClientSerializer
    queryset = catClient.objects.all()
    
class BusinessContactViewSet(viewsets.ModelViewSet):
    
    serializer_class = BusinessContactSerializer
    queryset = catBusinessContact.objects.all()
    
    
    
    


 