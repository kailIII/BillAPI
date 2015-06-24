# viewsets.py
from service.models import catKindService, catService, tblCategoryServices, tblServicesHistoryPrice, tblServiceDocumentDetails, tblServiceCost, tblServiceCostDetail, tblServiceManage, tblScheduleDate, tblScheduleDateDetail, catProviderService, catCompanyService
from service.serializers import KindServiceSerializer, ServiceSerializer, CategoryServicesSerializer, ServicesHistoryPriceSerializer, ServiceDocumentDetailsSerializer, ServiceCostSerializer, ServiceCostDetailSerializer, ServiceManageSerializer, ScheduleDateSerializer, ScheduleDateDetailSerializer, ProviderServiceSerializer, CompanyServiceSerializer 
from rest_framework import viewsets
 
 #class
 

class KindServiceViewSet(viewsets.ModelViewSet):
    
    serializer_class = KindServiceSerializer
    queryset = catKindService.objects.all()
    
class ServiceViewSet(viewsets.ModelViewSet):
    
    serializer_class = ServiceSerializer
    queryset = catService.objects.all()
    
class CategoryServicesViewSet(viewsets.ModelViewSet):
    
    serializer_class = CategoryServicesSerializer
    queryset = tblCategoryServices.objects.all()
    
class ServicesHistoryPriceViewSet(viewsets.ModelViewSet):
    
    serializer_class = ServicesHistoryPriceSerializer
    queryset = tblServicesHistoryPrice.objects.all()
    
class ServiceDocumentDetailsViewSet(viewsets.ModelViewSet):
    
    serializer_class = ServiceDocumentDetailsSerializer
    queryset = tblServiceDocumentDetails.objects.all()
    
class ServiceCostViewSet(viewsets.ModelViewSet):
    
    serializer_class = ServiceCostSerializer
    queryset = tblServiceCost.objects.all()
    
class ServiceCostDetailViewSet(viewsets.ModelViewSet):
    
    serializer_class = ServiceCostDetailSerializer
    queryset = tblServiceCostDetail.objects.all()
    
class ServiceManageViewSet(viewsets.ModelViewSet):
    
    serializer_class = ServiceManageSerializer
    queryset = tblServiceManage.objects.all()
    
class ScheduleDateViewSet(viewsets.ModelViewSet):
    
    serializer_class = ScheduleDateSerializer
    queryset = tblScheduleDate.objects.all()
    
class ScheduleDateDetailViewSet(viewsets.ModelViewSet):
    
    serializer_class = ScheduleDateDetailSerializer
    queryset = tblScheduleDateDetail.objects.all()
    
class ProviderServiceViewSet(viewsets.ModelViewSet):
    
    serializer_class = ProviderServiceSerializer
    queryset = catProviderService.objects.all()
    
class CompanyServiceViewSet(viewsets.ModelViewSet):
    
    serializer_class = CompanyServiceSerializer
    queryset = catCompanyService.objects.all()
    





 
    
    
    


 