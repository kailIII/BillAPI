# serializers.py
from main.models import catCity, catCountry, tblBDP, catMail, catPhone, catAddress, catWebsite, catHalls, catArea, catAppointment, catCategorySP, catCoin, tblCoinHistory
from rest_framework import serializers

 #Class

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = catCountry
        fields = ('idCountry', 'code', 'name', 'note', 'create', 'update')
 
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = catCity
        fields = ('idCity', 'idcountry', 'name', 'note', 'create', 'update')
        
class BDPSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblBDP
        fields = ('idBDP', 'photo', 'idCard', 'postal', 'name', 'surname', 'birthdate')

class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = catMail
        fields = ('idMail', 'idBDP', 'kind', 'mail', 'isActive', 'note', 'create', 'update')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = catAddress
        fields = ('idAddress', 'idBDP', 'idCity', 'kind', 'address', 'isActive', 'note', 'create', 'update')
        
class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = catPhone
        fields = ('idPhone', 'idBDP', 'kind', 'scope', 'area', 'number', 'isActive', 'note', 'create', 'update')
        
class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = catWebsite
        fields = ('idWebsite', 'idBDP', 'name', 'address', 'isActive', 'note', 'create', 'update')        
 
class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = catHalls
        fields = ('idHall', 'idCity', 'name', 'address', 'quantity', 'beginHour', 'endHour', 'state')
 
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = catArea
        fields = ('idArea', 'name', 'shortName', 'note', 'create', 'update')

class AppointmentSerializer(serializers.ModelSerializer):
   class Meta:
        model = catAppointment
        fields = ('idAppointment', 'idArea', 'name', 'note', 'create', 'update')

class CategorySPSerializer(serializers.ModelSerializer):
   class Meta:
        model = catCategorySP
        fields = ('idCategorySP','name', 'note', 'create', 'update')
        
class CoinSerializer(serializers.ModelSerializer):
   class Meta:
        model = catCoin
        fields = ('idCoin', 'idCountry', 'name', 'symbol', 'isMain', 'note', 'create', 'update')
        
class CoinHistorySerializer(serializers.ModelSerializer):
   class Meta:
        model = tblCoinHistory
        fields = ('idCoinHistory', 'idCoin', 'rateChange', 'isActive', 'note', 'create', 'update')

 
 
 
 
        
        
        