from django.db import models
from main.models import base, tblBDP, catCoin
from company.models import tblDocument, catMembership

# Create your models here.s

class catBank(base):
    idBank  = models.AutoField(primary_key=True)
    idBDP = models.ForeignKey(tblBDP)
    shortName = models.CharField(max_length = 30, null = True, blank = True)
    isActive = models.BooleanField(default = 1, null = False, blank = False)

    def __str__(self):
    	return self.idBDP


class tblBankControl(base):
    idBankControl  = models.AutoField(primary_key=True)
    idMembership = models.ForeignKey(catMembership)
    idBank = models.ForeignKey(catBank)
    idCoin = models.ForeignKey(catCoin)
    noAccount = models.CharField(max_length = 40)
    total  = models.FloatField(null = False, blank = False)

    def __str__(self):
    	return '%s - %s' %(self.idMembership, self.idBank)


class tblBankControlDetail(models.Model):
    idBankControlDetail  = models.AutoField(primary_key=True)
    idBankControl  = models.ForeignKey(tblBankControl)
    idDocument  = models.ForeignKey(tblDocument)

    def __str__(self):
    	return '%s - %s' %(self.idBankControl, self.idDocument)


class tblBankControlAdjust(models.Model):
    idBankControlAdjust  = models.AutoField(primary_key=True)
    idBankControl = models.ForeignKey(tblBankControl)
    adjust = models.FloatField(null = False, blank = False)
    adjustDetail = models.CharField(max_length = 255)

    def __str__(self):
    	return self.idBankControl