from django.db import models
from main.models import base, tblBDP, catHalls


# Create your models here.

class catProvider(tblBDP):
    idProvider  = models.AutoField(primary_key=True)
    isPerson = models.BooleanField(default = 0, null = False, blank = False)
    isActive = models.BooleanField(default = 1, null = False, blank = False)
    beginDate = models.DateField(null= True, blank = True)
    note = models.CharField(max_length = 255, null = True, blank = True)
    create = models.DateField(auto_now_add = True, null = False, blank = False)
    update = models.DateField(auto_now = True, null = False, blank = False)
    hall = models.ManyToManyField(catHalls, through = 'tblProviderHalls')

    def __str__(self):
    	return '%s - %s' %(self.name, self.surname)


class tblProviderHalls(models.Model):
#    idProviderHall  = models.AutoField(primary_key=True)
    idHall = models.ForeignKey(catHalls)
    idProvider = models.ForeignKey(catProvider)
    note = models.CharField(max_length = 255, null = True, blank = True)
    create = models.DateField(auto_now_add = True, null = False, blank = False)
    update = models.DateField(auto_now = True, null = False, blank = False)
    
    def __str__(self):
    	return '%s - %s' %(self.name, self.idProvider)
 