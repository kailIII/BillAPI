# serializers.py
from client.models import catKindClient, catClient, catBusinessContact
from rest_framework import serializers

 #Class


class KindClientSerializer(serializers.ModelSerializer):
    class Meta:
        model =  catKindClient
        fields = ('idKindClient', 'name', 'credictTimeAverage', 'credictAverage', 'discountAverage', 'note', 'create', 'update')
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model =  catClient
        fields = ('idClient', 'idKindClient', 'photo', 'idCard', 'postal', 'name', 'surname', 'birthdate', 'isPerson', 'isActive', 'beginDate', 'note', 'create', 'update')
        
class BusinessContactSerializer(serializers.ModelSerializer):
    class Meta:
        model =  catBusinessContact
        fields = ('idBusinessContact', 'idAppointment', 'idClient', 'isPerson', 'isActive', 'note', 'create', 'update')
        
        
        
        