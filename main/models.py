from django.db import models
from django.conf import settings

UPLOADS_DIR = getattr(settings, "UPLOADS_DIR", "uploads")

# Create your models here.
class base(models.Model):
    note = models.CharField(max_length = 255, null = True, blank = True)
    create = models.DateField(auto_now_add = True, null = False, blank = False)
    update = models.DateField(auto_now = True, null = False, blank = False)
    
    class Meta:
        abstract = True


class catCountry(base):
    idCountry = models.AutoField(primary_key=True)
    code = models.PositiveIntegerField(null = True, blank = True)
    name = models.CharField(max_length = 75, null = False, blank = False)
    
    def __str__(self):
        return self.name


class catCity(base):
    idCity = models.AutoField(primary_key=True)
    idcountry = models.ForeignKey(catCountry)
    name = models.CharField(max_length = 75, null = False, blank = False)
    
    def __str__(self):
        return self.name


class tblBDP(models.Model):
    idBDP = models.AutoField(primary_key=True)
    photo = models.CharField(max_length = 255, null = True, blank = True)
    idCard = models.CharField(max_length = 25, null = True, blank = True)
    postal = models.PositiveIntegerField(null = True, blank = True)
    name = models.CharField(max_length = 75, null = False, blank = False)
    surname = models.CharField(max_length = 75, null = False, blank = False)
    birthdate = models.DateField()
    #idcity = models.ForeignKey(catCity)
    idAddress = models.ManyToManyField(catCity, through = 'catAddress')

    def __str__(self):
        return '%s - %s' %(self.name, self.surname)

  #  class Meta:
  #     abstract = True


class catAddress(base):
    idAddress  = models.AutoField(primary_key=True)
    idBDP = models.ForeignKey(tblBDP)
    idCity = models.ForeignKey(catCity)
    K_LIST = ((1, 'Principal'),(2,'Secundaria'),(3,'Otra'))
    kind = models.IntegerField(choices = K_LIST, default = 1, null = False, blank = False)
    address = models.CharField(max_length = 255, null = False, blank = False)
    isActive = models.BooleanField(default = 1, null = False, blank = False)

    def __str__(self):
        return '%s, %s' %(self.address, self.idCity)
   

class catMail(base):
    idMail  = models.AutoField(primary_key=True)
    idBDP = models.ForeignKey(tblBDP)
    K_LIST = ((1,'Private'),(2,'Public'),(3,'Coorporative')) 
    kind = models.IntegerField(choices = K_LIST, null = False, blank = False)
    mail = models.CharField(max_length = 40, null = False, blank = False)
    isActive = models.BooleanField(default = 1, null = False, blank = False)

    def __str__(self):
        return self.mail
   
   
class catPhone(base):
    idPhone  = models.AutoField(primary_key=True)
    idBDP = models.ForeignKey(tblBDP)
    K_LIST = ((1,'Movil'),(2,'Fijo')) 
    kind = models.IntegerField(choices = K_LIST, default = 1, null = False, blank = False) 
    S_LIST = ((1,'Casa'),(2,'Trabajo'),(3,'Principal'),(4,'Otro'))
    scope = models.IntegerField(choices = S_LIST, default = 1, null = False, blank = False)
    area = models.PositiveIntegerField(null = True, blank = True)
    number = models.IntegerField() 
    isActive = models.BooleanField(default = 1, null = False, blank = False)

    def __str__(self):
        return '(%s) - %s' %(self.area, self.number)

    def _get_phone_number_(self):
    	return '(%s) - %s' %(self.area, self.number)
    
    get_phone = property(_get_phone_number_)


class catWebsite(base):
    idWebsite = models.AutoField(primary_key=True)
    idBDP = models.ForeignKey(tblBDP)
    name = models.CharField(max_length = 50, null = True, blank = True)
    address = models.CharField(max_length = 100, null = False, blank = False)
    isActive = models.BooleanField(default = 1, null = False, blank = False)

    def __str__(self):
    	return '%s - %s' %(self.name, self.address)


 #----------------- --------------------------------------------------------------
class catHalls(models.Model):
    idHall = models.AutoField(primary_key=True)
    idCity  = models.ForeignKey(catCity)
    name = models.CharField(max_length = 50,  null = False, blank = False)
    address = models.CharField(max_length = 255,  null = False, blank = False)
    quantity = models.PositiveIntegerField(null = True, blank = True)
    beginHour = models.TimeField(null = True, blank = True)
    endHour = models.TimeField(null = True, blank = True)
    S_LIST = ((1,'Libre'),(2,'Ocupado'),(3,'Mantenimiento'),(4,'Otro'))
    state = models.IntegerField(choices = S_LIST, default = 1, null = False, blank = False)
    
    def __str__(self):
        return self.name
    
#    class Meta:
#        abstract = True


class catArea(base):
    idArea = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50,  null = False, blank = False)
    shortName = models.CharField(max_length = 20,  null = True, blank = True)
    
    def __str__(self):
    	return self.name


class catAppointment(base):
    idAppointment = models.AutoField(primary_key=True)
    idArea  = models.ForeignKey(catArea)
    name = models.CharField(max_length = 50,  null = False, blank = False)
    
    def __str__(self):
    	return 'Area: %s - %s' %(self.name, self.idArea)


class catCategorySP(base):
	idCategorySP = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 50,  null = False, blank = False)

	def __str__(self):
		return self.name
    

class catCoin(base):
    idCoin = models.AutoField(primary_key=True)
    idCountry = models.ForeignKey(catCountry) 
    name = models.CharField(max_length = 35, null = False, blank = False)
    symbol = models.CharField(max_length = 4,  null = False, blank = False)
    isMain = models.BooleanField(default = 0, null = False, blank = False)
    
    def __str__(self):
    	return self.name


class tblCoinHistory(base):
    idCoinHistory = models.AutoField(primary_key=True)
    idCoin = models.ForeignKey(catCoin)
    rateChange = models.FloatField( null = False, blank = False)
    isActive = models.BooleanField(default = 1, null = False, blank = False)

    def __str__(self):
    	return '%s - %s' %(self.idCoin, self.rateChange)
 
