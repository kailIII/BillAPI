# viewsets.py
from bank.models import catBank, tblBankControl, tblBankControlDetail, tblBankControlAdjust
from bank.serializers import BankSerializer, BankControlSerializer, BankControlDetailSerializer, BankControlAdjustSerializer 
from rest_framework import viewsets
 
 #class
 
class BankViewSet(viewsets.ModelViewSet):
    
    serializer_class = BankSerializer
    queryset = catBank.objects.all()

class BankControlViewSet(viewsets.ModelViewSet):
    
    serializer_class = BankControlSerializer
    queryset = tblBankControl.objects.all()

class BankControlDetailViewSet(viewsets.ModelViewSet):
    
    serializer_class = BankControlDetailSerializer
    queryset = tblBankControlDetail.objects.all()

class BankControlAdjustViewSet(viewsets.ModelViewSet):
    
    serializer_class = BankControlAdjustSerializer
    queryset = tblBankControlAdjust.objects.all()
 
    
    
    


 