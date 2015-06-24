# serializers.py
from provider.models import catProvider, tblProviderHalls
from rest_framework import serializers

 #Class

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model =  catProvider
        fields = ('idProvider','photo', 'idCard', 'postal', 'name', 'surname', 'birthdate','isPerson','isActive','beginDate','note','create','update')
        
class ProviderHallsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tblProviderHalls
        fields = ('idHall','idProvider','note','create','update')
        
 
 
        
        
        