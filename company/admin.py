from django.contrib import admin
from company.models import catCompany, tblCompanyHalls, catEmployee, tblEmployeeHistory, catMembership, tblDocument, tlbDocumentDetailCredict

# Register your models here.

admin.site.register(catCompany)
admin.site.register(tblCompanyHalls)
admin.site.register(catEmployee)
admin.site.register(tblEmployeeHistory)
admin.site.register(catMembership)

#-----------------------------
admin.site.register(tblDocument)
admin.site.register(tlbDocumentDetailCredict)