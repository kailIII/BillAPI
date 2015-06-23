# serializers.py
from article.models import catBrand, catModel, catArticle, tblBatch, catPresentation, tblArticlePresentation, tblCategoryArticle, tblArticleHistoryPrice, tblArticleInventory, catCompanyArticle, catProviderArticle, tblArticleDocumentDetails
from rest_framework import serializers

 #Class


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model =  catBrand
        fields = ('idBrand', 'name', 'note', 'create', 'update')
        
class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =  catModel
        fields = ('idModel', 'idBrand', 'model', 'note', 'create', 'update')
        
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model =  catArticle
        fields = ('idArticle', 'idModel', 'name', 'codeBar', 'measureList', 'measure', 'note', 'create', 'update')

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model =  tblBatch
        fields = ('idBatch', 'noBatch', 'idArticle', 'createDate', 'expirationDate', 'quantity', 'isLapsed', 'isActive', 'note', 'create', 'update')
                
class PresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model =  catPresentation
        fields = ('idPresentation', 'name', 'note', 'create', 'update')
        
class ArticlePresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblArticlePresentation
        fields = ('idArticlePresentation', 'idArticle', 'idPresentation', 'note', 'create', 'update')
        
class CategoryArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblCategoryArticle
        fields = ('idCategoryArticle', 'idArticle', 'idCategorySP', 'note', 'create', 'update')
        
class ArticleHistoryPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblArticleHistoryPrice
        fields = ('idArticleHistoryPrice', 'idArticle', 'idCoin', 'price', 'hasTax', 'isActive', 'note', 'create', 'update')
        
class ArticleInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = tblArticleInventory
        fields = ('idArticleInventory', 'idArticle', 'sMin', 'sMax', 'existence', 'availability', 'create', 'update')
        
class CompanyArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = catCompanyArticle
        fields = ('idCompanyArticle', 'idCompany', 'idArticle', 'note', 'create', 'update')
        
class ProviderArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = catProviderArticle
        fields = ('idProviderArticle', 'idProvider', 'idArticle', 'note', 'create', 'update')
 
class ArticleDocumentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = tblArticleDocumentDetails
        fields = ('idArticleDocumentDetails', 'idDocument', 'idArticle', 'realPrice', 'quantity', 'discount', 'tax')       
 

 
 
        
        
        