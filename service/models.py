from django.db import models
from main.models import base, catCategorySP, catCoin, catHalls
from company.models import catCompany, tblDocument, catEmployee
from provider.models import catProvider
from purchase.models import tblPurchase


# Create your models here.

class catKindService(base):
    idKindService = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 70,  null = False, blank = False)

    def __str__(self):
    	return self.name


class catService(base):
    idService = models.AutoField(primary_key=True)
    idKindService = models.ForeignKey(catKindService)
    name = models.CharField(max_length = 70,   null = False, blank = False)
    shortname = models.CharField(max_length = 15,  null = True, blank = True)
    duration  = models.PositiveIntegerField(null = True, blank = True)

    def __str__(self):
    	return self.name


class tblCategoryServices(base):
    idCategoryServices = models.AutoField(primary_key=True)
    idCategorySP = models.ForeignKey(catCategorySP)
    idService = models.ForeignKey(catService)

    def __str__(self):
    	return '%s - %s' %(self.idCategorySP, self.idService)


class tblServicesHistoryPrice(base):
    idServicesHistoryPrice = models.AutoField(primary_key=True)
    idService = models.ForeignKey(catService)
    idCoin = models.ForeignKey(catCoin)
    price = models.FloatField(null = False, blank = False)
    hasTax = models.BooleanField(default = 0, null = False, blank = False)
    isActive = models.BooleanField(default = 1, null = False, blank = False)
    
    def __str__(self):
    	return '%s - %s - %s' %(self.idService, self.idCoin, self.price)

#---------------------------------------------------------------------------------
class tblServiceDocumentDetails(base):
    idServiceDocumentDetails = models.AutoField(primary_key=True)
    idDocument = models.ForeignKey(tblDocument)
    idservice  = models.ForeignKey(catService)
    realPrice = models.FloatField(null = True, blank = True)
    quantity  = models.FloatField(null = False, blank = False)
    discount = models.FloatField(null = True, blank = True)
    tax = models.FloatField(null = True, blank = True)

    def __str__(self):
    	return '%s - %s' %(self.idDocument, self.service)

#---------------------------------------------------------------------------------
class tblServiceCost(base):
    idServiceCost = models.AutoField(primary_key=True)
    idServiceDocumentDetails = models.ForeignKey(tblServiceDocumentDetails)
    isActive  = models.BooleanField(default = 1, null = False, blank = False)

    def __str__(self):
    	return self.idServiceDocumentDetails



class tblServiceCostDetail(base):
    idServiceCostDetail = models.AutoField(primary_key=True)
    idServiceCost = models.ForeignKey(tblServiceCost)
    idPurchase = models.ForeignKey(tblPurchase)

    def __str__(self):
        return '%s - %s' %(self.idPurchase, self.idServiceCost)

   

class tblServiceManage(models.Model):
    idServiceManage = models.AutoField(primary_key=True)
    idServiceCost = models.ForeignKey(tblServiceCost)
    S_LIST = ((1,'Ejecucion'),(2,'Preparacion'),(3,'Culminado'),(4,'Otro'))
    state = models.IntegerField(choices = S_LIST, default = 2, null = False, blank = False)
    create = models.DateField(auto_now_add = True, null = False, blank = False)
    update = models.DateField(auto_now = True, null = False, blank = False)

    def __str__(self):
    	return '%s - %s' %(self.idServiceCost, self.state)


class tblScheduleDate(base):
    idScheduleDate = models.AutoField(primary_key=True)
    idServiceManage = models.ForeignKey(tblServiceManage)
    name = models.CharField(max_length = 90, null = False, blank = False)
    date = models.DateField(null = False, blank = False)

    def __str__(self):
    	return '%s - %s - %s' %(self.idServiceManage, self.name, self.date)
   

class tblScheduleDateDetail(models.Model):
    idScheduleDateDetail = models.AutoField(primary_key=True)
    idScheduleDate = models.ForeignKey(tblScheduleDate)
    idHall = models.ForeignKey(catHalls)
    idEmployee = models.ForeignKey(catEmployee)
    name = models.CharField(max_length = 90, null = True, blank = True)
    beginHour  = models.TimeField(null = True, blank = True)
    endHour  = models.TimeField(null = True, blank = True)
    create = models.DateField(auto_now_add = True, null = False, blank = False)
    update = models.DateField(auto_now = True, null = False, blank = False)

    def __str__(self):
    	return '%s - %s - %s - %s' %(self.idHall, self.idScheduleDate, self.idEmployee, self,name)


class catProviderService(base):
    idProviderArticle  = models.AutoField(primary_key=True)
    idProvider = models.ForeignKey(catProvider)
    idService = models.ForeignKey(catService)

    def __str__(self):
        return '%s - %s' %(self.idProvider, self.idService)


class catCompanyService(base):  
    idCompanyService = models.AutoField(primary_key=True)
    idCompany = models.ForeignKey(catCompany)
    idService = models.ForeignKey(catService)

    def __str__(self):
    	return '%s - %s' %(self.idCompany, self.idService)
    	