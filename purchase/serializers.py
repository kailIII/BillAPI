# serializers.py
from purchase.models import tblPurchase
from rest_framework import serializers

 #Class

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tblPurchase
        fields = ('idPurchase','idDocument', 'idProvider', 'noDocument','note','create','update')
        

 
        
        
        