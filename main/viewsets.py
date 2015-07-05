# viewsets.py

#---------------------------
from django.contrib.auth.models import User
from .models import catCity, catCountry, tblBDP, catMail, catPhone, catAddress, catWebsite, catHalls, catArea, catAppointment, catCategorySP, catCoin, tblCoinHistory
from .serializers import UserSerializer, CountrySerializer, CitySerializer, BDPSerializer, MailSerializer, AddressSerializer, PhoneSerializer, WebsiteSerializer, HallSerializer, AreaSerializer, AppointmentSerializer, CategorySPSerializer, CoinSerializer, CoinHistorySerializer
from rest_framework import viewsets
from rest_framework import permissions
from main.permissions import IsOwner

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
 
 #class
class UserViewSet(viewsets.ModelViewSet):
    
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'

 
class CountryViewSet(viewsets.ModelViewSet):
    
    serializer_class = CountrySerializer
    queryset = catCountry.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)
 
 
class CityViewSet(viewsets.ModelViewSet):
    
    serializer_class = CitySerializer
    queryset = catCity.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)
    
    
class BDPViewSet(viewsets.ModelViewSet):
    
    serializer_class = BDPSerializer
    queryset = tblBDP.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)   


class MailViewSet(viewsets.ModelViewSet):
    
    serializer_class = MailSerializer
    queryset = catMail.objects.all()
    permission_classes = (IsAuthenticated, IsOwner) 


class AddressViewSet(viewsets.ModelViewSet):
    
    serializer_class = AddressSerializer
    queryset = catAddress.objects.all()
    
class PhoneViewSet(viewsets.ModelViewSet):
    
    serializer_class = PhoneSerializer
    queryset = catPhone.objects.all()
    
class WebsiteViewSet(viewsets.ModelViewSet):
    
    serializer_class = WebsiteSerializer
    queryset = catWebsite.objects.all()


class HallViewSet(viewsets.ModelViewSet):
    
    serializer_class = HallSerializer
    queryset = catHalls.objects.all()
    

class AreaViewSet(viewsets.ModelViewSet):
    
    serializer_class = AreaSerializer
    queryset = catArea.objects.all()
    

class AppointmentViewSet(viewsets.ModelViewSet):
    
    serializer_class = AppointmentSerializer
    queryset = catAppointment.objects.all()
    

class CategorySPViewSet(viewsets.ModelViewSet):
    
    serializer_class = CategorySPSerializer
    queryset = catCategorySP.objects.all()
    
    
class CoinViewSet(viewsets.ModelViewSet):
    
    serializer_class = CoinSerializer
    queryset = catCoin.objects.all()
    

class CoinHistoryViewSet(viewsets.ModelViewSet):
    
    serializer_class = CoinHistorySerializer
    queryset = tblCoinHistory.objects.all()



