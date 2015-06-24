# serializers.py
from service.models import catKindService, catService, tblCategoryServices, tblServicesHistoryPrice, tblServiceDocumentDetails, tblServiceCost, tblServiceCostDetail, tblServiceManage, tblScheduleDate, tblScheduleDateDetail, catProviderService, catCompanyService
from rest_framework import serializers

 #Class

class KindServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model =  catKindService
        fields = ('idKindService','name','note','create','update') 
        
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model =  catService
        fields = ('idService','idKindService','name','shortname','duration','note','create','update') 
        
class CategoryServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tblCategoryServices
        fields = ('idCategoryServices','idCategorySP','idService','note','create','update') 
        
class ServicesHistoryPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tblServicesHistoryPrice
        fields = ('idServicesHistoryPrice','idService','idCoin','price','hasTax','isActive','note','create','update') 
        
class ServiceDocumentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tblServiceDocumentDetails
        fields = ('idServiceDocumentDetails','idDocument','idservice','realPrice','quantity','discount','tax','note','create','update') 
        
class ServiceCostSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tblServiceCost
        fields = ('idServiceCost','idServiceDocumentDetails','isActive','note','create','update') 
        
class ServiceCostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tblServiceCostDetail
        fields = ('idServiceCostDetail','idServiceCost','idPurchase','note','create','update') 
        
class ServiceManageSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tblServiceManage
        fields = ('idServiceManage','idServiceCost','state','create','update') 
        
class ScheduleDateSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tblScheduleDate
        fields = ('idScheduleDate','idServiceManage','name','date','note','create','update') 
        
class ScheduleDateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tblScheduleDateDetail
        fields = ('idScheduleDateDetail','idScheduleDate','idHall','idEmployee','name','beginHour','endHour','create','update') 
        
class ProviderServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model =  catProviderService
        fields = ('idProviderArticle','idProvider','idService','note','create','update') 
        
class CompanyServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model =  catCompanyService
        fields = ('idCompanyService','idCompany','idService','note','create','update') 
 
        
        
        