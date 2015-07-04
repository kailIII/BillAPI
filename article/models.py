from django.db import models
from main.models import base, catCategorySP, catCoin
from company.models import tblDocument, catCompany
from provider.models import catProvider

# Create your models here.

class catBrand(base):
    idBrand = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 45, null = False, blank = False)
    
    def __str__(self):
    	return self.name

class catModel(base):
    idModel = models.AutoField(primary_key=True)
    idBrand = models.ForeignKey(catBrand)
    model = models.CharField(max_length = 35, null = False, blank = False)

    def __str__(self):
    	return '%s - %s' %(self.idBrand, self.model)
    

class catArticle(base):
    idArticle = models.AutoField(primary_key=True)
    idModel = models.ForeignKey(catModel)
    name = models.CharField(max_length = 50, null = False, blank = False)
    codeBar = models.CharField(max_length = 100, null = True, blank = True)
    M_LIST = ((1,'gramos'),(2,'Kilogramos'),(3,'Onza'), (4,'Libra'), (5, 'Litro'), (6, 'Galon'), (7,'Quintal'))
    measureList = models.IntegerField(choices = M_LIST, default = 1, null = False, blank = False)
    measure = models.FloatField( null = True, blank = True)
    category = models.ManyToManyField(catCategorySP, through = 'tblCategoryArticle')
    idDocument = models.ManyToManyField(tblDocument, through = 'tblArticleDocumentDetails')

    def __str__(self):
    	return '%s - %s' %(self.idModel, self.name)


class tblBatch(base):
    idBatch = models.AutoField(primary_key=True)
    noBatch  = models.CharField(max_length = 20, null = False, blank = False)
    idArticle  = models.ForeignKey(catArticle)
    createDate  = models.DateField(null= True, blank = True)
    expirationDate  = models.DateField(null= True, blank = True)
    quantity = models.PositiveIntegerField(null = True, blank = True)
    isLapsed  = models.BooleanField(default = 0, null = False, blank = False)
    isActive  = models.BooleanField(default = 1, null = False, blank = False)

    def __str__(self):
    	return '%s - %s' %(self.idArticle, self.noBatch)



class catPresentation(base):
    idPresentation = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50, null = False, blank = False)
    article = models.ManyToManyField(catArticle, through = 'tblArticlePresentation')

    def __str__(self):
    	return self.name


class tblArticlePresentation(base):
    idArticlePresentation = models.AutoField(primary_key=True)
    idArticle = models.ForeignKey(catArticle)
    idPresentation = models.ForeignKey(catPresentation)
    
    def __str__(self):
    	return '%s - %s' %(self.idPresentation, self.idArticle)


class tblCategoryArticle(base):
    idCategoryArticle = models.AutoField(primary_key=True)
    idCategorySP  = models.ForeignKey(catCategorySP)
    idArticle  = models.ForeignKey(catArticle)

    def __str__(self):
    	return '%s - %s' %(self.idCategorySP, self.idArticle)


class tblArticleHistoryPrice(base):
    idArticleHistoryPrice = models.AutoField(primary_key=True)
    idArticle = models.ForeignKey(catArticle)
    idCoin = models.ForeignKey(catCoin)
    price = models.FloatField(null = False, blank = False)
    hasTax = models.BooleanField(default = 0, null = False, blank = False)
    isActive = models.BooleanField(default = 1, null = False, blank = False)
    
    def __str__(self):
    	return '%s - %s - %s' %(self.idArticle, self.idCoin, self.price)


class tblArticleInventory(models.Model):
    idArticleInventory = models.AutoField(primary_key=True)
    idArticle = models.ForeignKey(catArticle)
    sMin = models.IntegerField(null = False, blank = False)
    sMax = models.IntegerField(null = False, blank = False)
    existence = models.IntegerField(null = False, blank = False)
    availability = models.IntegerField(null = False, blank = False)
    create = models.DateField(auto_now_add = True, null = False, blank = False)
    update = models.DateField(auto_now = True, null = False, blank = False)

    def __str__(self):
    	return '%s - Existence: %s - Availability: %s' %(self.idArticle, self.existence, self.availability)
        
#---------------------------------------------------------------------------------
class catCompanyArticle(base):
    idCompanyArticle = models.AutoField(primary_key=True)
    idCompany = models.ForeignKey(catCompany)
    idArticle = models.ForeignKey(catArticle)
    
    def __str__(self):
    	return self.idArticle
   

class catProviderArticle(base):
    idProviderArticle  = models.AutoField(primary_key=True)
    idProvider = models.ForeignKey(catProvider)
    idArticle  = models.ForeignKey(catArticle)
    
    def __str__(self):
    	return self.idArticle


class tblArticleDocumentDetails(models.Model):
    idArticleDocumentDetails = models.AutoField(primary_key=True)
    idDocument = models.ForeignKey(tblDocument)
    idArticle = models.ForeignKey(catArticle)
    realPrice = models.FloatField(null = True, blank = True)
    quantity = models.FloatField(null = True, blank = False)
    discount = models.FloatField(null = False, blank = False)
    tax = models.FloatField(null = True, blank = True)
    
    def __str__(self):
        return self.idArticle

