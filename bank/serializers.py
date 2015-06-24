# serializers.py
from bank.models import catBank, tblBankControl, tblBankControlDetail, tblBankControlAdjust
from rest_framework import serializers

 #Class



class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model =  catBank
        fields = ('idBank','idBDP','shortName','isActive', 'note','create','update')
        
class BankControlSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tblBankControl
        fields = ('idBankControl','idMembership','idBank','idCoin','noAccount','total', 'note','create','update')
        
class BankControlDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tblBankControlDetail
        fields = ('idBankControlDetail','idBankControl','idDocument')
        
class BankControlAdjustSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tblBankControlAdjust
        fields = ('idBankControlAdjust','idBankControl','adjust','adjustDetail')

 
 
        
        
        