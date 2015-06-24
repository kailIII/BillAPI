# viewsets.py
from order.models import tblOrder
from order.serializers import OrderSerializer 
from rest_framework import viewsets
 
 #class
 
class OrderViewSet(viewsets.ModelViewSet):
    
    serializer_class = OrderSerializer
    queryset = tblOrder.objects.all()


 
    
    
    


 