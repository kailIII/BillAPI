from django.contrib import admin
from main.models import catCity, catCountry, tblBDP, catMail, catPhone, catAddress, catWebsite, catHalls, catArea, catAppointment, catCategorySP, catCoin, tblCoinHistory
#from client.models import kindClient, client, company, area, responsible, companyContact
# Register your models here.


#--------------main---------------
admin.site.register(catCountry)
admin.site.register(catCity)
#admin.site.register(tblBDP)
admin.site.register(catMail)
admin.site.register(catPhone)
admin.site.register(catAddress)
admin.site.register(catWebsite)

#-----------------------------
admin.site.register(catHalls)
admin.site.register(catCategorySP)
admin.site.register(catAppointment)
admin.site.register(catArea)
admin.site.register(catCoin)
admin.site.register(tblCoinHistory)

