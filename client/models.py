from django.db import models
from main.models import base, tblBDP, catAppointment
# Create your models here.

class catKindClient(base):
    idKindClient = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 35, null = False, blank = False)
    credictTimeAverage = models.PositiveIntegerField(default = 15, null = True, blank = True)
    credictAverage = models.FloatField( null = True, blank = True)
    discountAverage = models.FloatField( null = True, blank = True)

    def __str__(self):
    	return self.name


class catClient(tblBDP):
    idClient = models.AutoField(primary_key=True)
    idKindClient = models.ForeignKey(catKindClient)
    isPerson = models.BooleanField(default = 0, null = False, blank = False)
    isActive = models.BooleanField(default = 1, null = False, blank = False)
    beginDate = models.DateField(null= True, blank = True)
    note = models.CharField(max_length = 255, null = True, blank = True)
    create = models.DateField(auto_now_add = True, null = False, blank = False)
    update = models.DateField(auto_now = True, null = False, blank = False)
    contact = models.ManyToManyField(catAppointment, through = 'catBusinessContact')

    def __str__(self):
    	return '%s %s' %(self.name, self.surname)


class catBusinessContact(tblBDP):
    idBusinessContact = models.AutoField(primary_key=True)
    idAppointment = models.ForeignKey(catAppointment)
    idClient = models.ForeignKey(catClient)
    isPerson = models.BooleanField(default = 0, null = False, blank = False)
    isActive = models.BooleanField(default = 1, null = False, blank = False)
    note = models.CharField(max_length = 255, null = True, blank = True)
    create = models.DateField(auto_now_add = True, null = False, blank = False)
    update = models.DateField(auto_now = True, null = False, blank = False)

    def __str__(self):
    	return '%s %s - %s - Cliente: %s' %(self.name, self.surname, self.idAppointment, self.idClient)

