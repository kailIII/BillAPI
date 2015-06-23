from django.db import models
from main.models import base
from company.models import tblDocument
from provider.models import catProvider

# Create your models here.

class tblPurchase(base):
    idPurchase = models.AutoField(primary_key=True)
    idDocument = models.ForeignKey(tblDocument)
    idProvider = models.ForeignKey(catProvider)
    noDocument = models.IntegerField(null = False, blank = False)
    
    def __str__(self):
    	return '%s - %s' %(self.idProvider, self.idDocument)
 

