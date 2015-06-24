# viewsets.py
from purchase.models import tblPurchase
from purchase.serializers import PurchaseSerializer 
from rest_framework import viewsets
 
 #class
 
class PurchaseViewSet(viewsets.ModelViewSet):
    
    serializer_class = PurchaseSerializer
    queryset = tblPurchase.objects.all()






 
    
    
    


 