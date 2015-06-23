from django.db import models
from main.models import base
from company.models import tblDocument
from client.models import catClient

# Create your models here.


class tblSale(base):
    idSale  = models.AutoField(primary_key=True)
    idDocument = models.ForeignKey(tblDocument)
    idClient = models.ForeignKey(catClient)
    noDocument = models.IntegerField(null= False, blank = False)

    def __str__(self):
    	return '%s - %s' %(self.idClient, self.idDocument)

