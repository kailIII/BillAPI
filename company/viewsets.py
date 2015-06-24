# viewsets.py
from company.models import catCompany, tblCompanyHalls, catEmployee, tblEmployeeHistory, catMembership, tblDocument, tlbDocumentDetailCredict
from company.serializers import CompanySerializer, CompanyHallsSerializer, EmployeeSerializer, EmployeeHistorySerializer, MembershipSerializer, DocumentSerializer, DocumentDetailCredictSerializer 
from rest_framework import viewsets
 
 #class
   
class CompanyViewSet(viewsets.ModelViewSet):
    
    serializer_class = CompanySerializer
    queryset = catCompany.objects.all()
    
class CompanyHallsViewSet(viewsets.ModelViewSet):
    
    serializer_class = CompanyHallsSerializer
    queryset = tblCompanyHalls.objects.all()
    
class EmployeeViewSet(viewsets.ModelViewSet):
    
    serializer_class = EmployeeSerializer
    queryset = catEmployee.objects.all()
    
class EmployeeHistoryViewSet(viewsets.ModelViewSet):
    
    serializer_class = EmployeeHistorySerializer
    queryset = tblEmployeeHistory.objects.all()
    
class MembershipViewSet(viewsets.ModelViewSet):
    
    serializer_class = MembershipSerializer
    queryset = catMembership.objects.all()
    
class DocumentViewSet(viewsets.ModelViewSet):
    
    serializer_class = DocumentSerializer
    queryset = tblDocument.objects.all()
    
class DocumentDetailCredictViewSet(viewsets.ModelViewSet):
    
    serializer_class = DocumentDetailCredictSerializer
    queryset = tlbDocumentDetailCredict.objects.all()
        
    


 