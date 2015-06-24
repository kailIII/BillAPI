# viewsets.py
from sale.models import tblSale
from sale.serializers import SaleSerializer 
from rest_framework import viewsets
 
 #class
 
class SaleViewSet(viewsets.ModelViewSet):
    
    serializer_class = SaleSerializer
    queryset = tblSale.objects.all()






 
    
    
    


 