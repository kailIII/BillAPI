# serializers.py
from order.models import tblOrder
from rest_framework import serializers

 #Class

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tblOrder
        fields = ('idOrder','idDocument','idClient','idClient', 'note','create','update')
        

 
 
        
        
        