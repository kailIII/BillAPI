from django.db import models
from main.models import base, tblBDP, catHalls, catAppointment

# Create your models here.

class catCompany(tblBDP):
    idCompany = models.AutoField(primary_key=True)
    about = models.CharField(max_length = 1000, null = True, blank = True)
    mision = models.CharField(max_length = 500, null = True, blank = True)
    vision = models.CharField(max_length = 500, null = True, blank = True)
    target = models.CharField(max_length = 500, null = True, blank = True)
    isActive = models.BooleanField(default = 1, null = False, blank = False)
    isMain = models.BooleanField(default = 0, null = False, blank = False)
    note = models.CharField(max_length = 255, null = True, blank = True)
    create = models.DateField(auto_now_add = True, null = False, blank = False)
    update = models.DateField(auto_now = True, null = False, blank = False)
    halls = models.ManyToManyField(catHalls, through = 'tblCompanyHalls')

    def __str__(self):
    	return '%s - %s' %(self.name, self.surname)


class tblCompanyHalls(models.Model):
#    idCompanyHall = models.AutoField(primary_key=True)
    idCompany = models.ForeignKey(catCompany)
    idHall = models.ForeignKey(catHalls)
    note = models.CharField(max_length = 255, null = True, blank = True)
    create = models.DateField(auto_now_add = True, null = False, blank = False)
    update = models.DateField(auto_now = True, null = False, blank = False)
        
    def __str__(self):
    	return '%s - %s' %(self.name, self.idCompany)


class catEmployee(tblBDP):
    idEmployee = models.AutoField(primary_key=True)
    note = models.CharField(max_length = 255, null = True, blank = True)
    create = models.DateField(auto_now_add = True, null = False, blank = False)
    update = models.DateField(auto_now = True, null = False, blank = False)
    history = models.ManyToManyField(catCompany, through = 'tblEmployeeHistory')
    
    def __str__(self):
    	return '%s %s' %(self.name, self.surname)


class tblEmployeeHistory(base):
    idEmployeeHistory = models.AutoField(primary_key=True)
    idCompany = models.ForeignKey(catCompany)
    idEmployee = models.ForeignKey(catEmployee)
    idAppointment = models.ForeignKey(catAppointment)
    isActive = models.BooleanField(default = 1, null = False, blank = False)
    
    def __str__(self):
    	return '%s - %s - %s' %(self.idCompany, self.idEmployee, self.idAppointment)

class catMembership(base):
    idMembership  = models.AutoField(primary_key=True)
    idCompany = models.ForeignKey(catCompany)
    shortName = models.CharField(max_length = 10, null = True, blank = True)

    def __str__(self):
        return self.shortName


#------------------------------------------------------------------------------
 
class tblDocument(models.Model):
    idDocument = models.AutoField(primary_key=True)
    idEmployee = models.ForeignKey(catEmployee)
    idMembership = models.ForeignKey(catMembership)
    MP_LIST = ((1, 'Efectivo'), (2,'Cheque'), (3,'Deposito'),(4,'Otro'))
    methodPayment = models.IntegerField(choices = MP_LIST, default = 1)
    methodPaymentDetail = models.CharField(max_length = 200, null = True, blank = True)
    DT_LIST = ((1,'Contado'),(2,'Credito'),(3,'Otro'))
    documentType = models.IntegerField(choices = DT_LIST, default = 1)
    CS_LIST = ((1,'Pagado'),(2,'Mora'),(3,'Credito'),(4,'Otro'))
    credicState = models.IntegerField(choices = CS_LIST, default = 1)
    discount = models.FloatField(null = False, blank = False)
    taxs = models.FloatField(null = False, blank = False)
    isNull = models.BooleanField(default=0, null=False, blank = False)
    create = models.DateField(auto_now_add = True, null = False, blank = False)
    update = models.DateField(auto_now = True, null = False, blank = False)
    
    def __str__(self):
        return '%s - %s - %s - %s' %(self.idDocument, self.idEmployee, self.idMembership, self.documentType)


class tlbDocumentDetailCredict(base):
    idDocumentDetailCredict = models.AutoField(primary_key=True)
    idDocument= models.ForeignKey(tblDocument)
    fee = models.FloatField(null = False, blank = False)
    MP_LIST = ((1, 'Efectivo'), (2,'Cheque'), (3,'Deposito'),(4,'Otro'))
    methodPayment = models.IntegerField(choices = MP_LIST, default = 1)
    methodPaymentDetail = models.CharField(max_length = 200, null = True, blank = True)
    payment = models.FloatField(null = False, blank = False)
    programDate = models.DateField(null = False, blank = False)
    paymentDate = models.DateField(null = True, blank = True)
    adjust = models.FloatField(null = True, blank = True)
    adjustDetail = models.CharField(max_length = 200, null = True, blank = True)
    
    def __str__(self):
        return '%s - %s' %(self.idDocument, self.payment    )
 