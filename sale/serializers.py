# serializers.py
from sale.models import tblSale
from rest_framework import serializers

 #Class

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tblSale
        fields = ('idSale','idDocument', 'idClient', 'noDocument','note','create','update')
        

 
        
        
        