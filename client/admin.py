from django.contrib import admin
from client.models import catKindClient, catClient, catBusinessContact
# Register your models here.

#--------------Client---------------
admin.site.register(catKindClient)
admin.site.register(catClient)
admin.site.register(catBusinessContact)
