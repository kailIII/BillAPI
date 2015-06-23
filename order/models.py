from django.db import models
from main.models import base
from company.models import tblDocument
from client.models import catClient

# Create your models here.
class tblOrder(base):
    idOrder  = models.AutoField(primary_key=True)
    idDocument = models.ForeignKey(tblDocument)
    idClient = models.ForeignKey(catClient)
    validityDays = models.PositiveIntegerField(default = 15, null = True, blank = True)

    def __str__(self):
    	return '%s - %s' %(self.idClient, self.idDocument)
