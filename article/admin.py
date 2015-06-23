from django.contrib import admin
from article.models import catBrand, catModel, catArticle, tblBatch, catPresentation, tblArticlePresentation, tblCategoryArticle, tblArticleHistoryPrice, tblArticleInventory, catCompanyArticle, catProviderArticle, tblArticleDocumentDetails

# Register your models here.
admin.site.register(catBrand)
admin.site.register(catModel)
admin.site.register(catArticle)
admin.site.register(tblBatch)
admin.site.register(catCompanyArticle)
admin.site.register(catPresentation)
admin.site.register(tblArticlePresentation)
admin.site.register(tblCategoryArticle)
admin.site.register(tblArticleHistoryPrice)
admin.site.register(tblArticleInventory)
admin.site.register(catProviderArticle)
admin.site.register(tblArticleDocumentDetails)