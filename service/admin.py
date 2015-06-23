from django.contrib import admin
from service.models import catKindService, catService, tblCategoryServices, tblServicesHistoryPrice, tblServiceDocumentDetails, tblServiceCost, tblServiceCostDetail, tblServiceManage, tblScheduleDate, tblScheduleDateDetail, catProviderService, catCompanyService

# Register your models here.
admin.site.register(catKindService)
admin.site.register(catService)
admin.site.register(tblCategoryServices)
admin.site.register(tblServicesHistoryPrice)
admin.site.register(tblServiceDocumentDetails)
admin.site.register(tblServiceCost)
admin.site.register(tblServiceCostDetail)
admin.site.register(tblServiceManage)
admin.site.register(tblScheduleDate)
admin.site.register(tblScheduleDateDetail)
admin.site.register(catProviderService)
admin.site.register(catCompanyService)
