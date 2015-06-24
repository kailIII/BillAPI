# viewsets.py
from provider.models import catProvider, tblProviderHalls
from provider.serializers import ProviderSerializer, ProviderHallsSerializer 
from rest_framework import viewsets
 
 #class
 
class ProviderViewSet(viewsets.ModelViewSet):
    
    serializer_class = ProviderSerializer
    queryset = catProvider.objects.all()


class ProviderHallsViewSet(viewsets.ModelViewSet):
    
    serializer_class = ProviderHallsSerializer
    queryset = tblProviderHalls.objects.all()



 
    
    
    


 