# serializers.py
from company.models import catCompany, tblCompanyHalls, catEmployee, tblEmployeeHistory, catMembership, tblDocument, tlbDocumentDetailCredict
from rest_framework import serializers

 #Class

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model =  catCompany
        fields =('idCompany','photo', 'idCard', 'postal', 'name', 'surname', 'birthdate','about','mision','vision','target','isActive','isMain','note','create','update') 
        
class CompanyHallsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tblCompanyHalls
        fields =('idCompany','idHall','note','create','update') 
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model =  catEmployee
        fields =('idEmployee','note','create','update') 
        
class EmployeeHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model =  tblEmployeeHistory
        fields =('idEmployeeHistory','idEmployee','idCompany','idAppointment','isActive','note','create','update') 
        
class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model =  catMembership
        fields =('idMembership','idCompany','shortName','note','create','update') 
        
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tblDocument
        fields =('idDocument','idEmployee','idMembership','methodPayment','methodPaymentDetail','documentType','credicState','discount','taxs','isNull','create','update') 
        
class DocumentDetailCredictSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tlbDocumentDetailCredict
        fields =('idDocumentDetailCredict','idDocument','fee','methodPayment','methodPaymentDetail','payment','programDate','paymentDate','adjust','adjustDetail','note','create','update') 
        


        
        
        