from django.contrib import admin
from bank.models import catBank, tblBankControl, tblBankControlDetail, tblBankControlAdjust

# Register your models here.
admin.site.register(catBank)
admin.site.register(tblBankControl)
admin.site.register(tblBankControlDetail)
admin.site.register(tblBankControlAdjust)