# viewsets.py
from article.models import catBrand, catModel, catArticle, tblBatch, catPresentation, tblArticlePresentation, tblCategoryArticle, tblArticleHistoryPrice, tblArticleInventory, catCompanyArticle, catProviderArticle, tblArticleDocumentDetails
from article.serializers import BrandSerializer, ModelSerializer, ArticleSerializer, BatchSerializer, PresentationSerializer, ArticlePresentationSerializer, CategoryArticleSerializer, ArticleHistoryPriceSerializer, ArticleInventorySerializer, CompanyArticleSerializer, ProviderArticleSerializer, ArticleDocumentDetailSerializer 
from rest_framework import viewsets
 
 #class
 
class BrandViewSet(viewsets.ModelViewSet):
    
    serializer_class = BrandSerializer
    queryset = catBrand.objects.all()
    
    
class ModelViewSet(viewsets.ModelViewSet):
    
    serializer_class = ModelSerializer
    queryset = catModel.objects.all()
    
    
class ArticleViewSet(viewsets.ModelViewSet):
    
    serializer_class = ArticleSerializer
    queryset = catArticle.objects.all()
    
    
class BatchViewSet(viewsets.ModelViewSet):
    
    serializer_class = BatchSerializer   
    queryset = tblBatch.objects.all()
    
class PresentationViewSet(viewsets.ModelViewSet):
    
    serializer_class = PresentationSerializer
    queryset = catPresentation.objects.all()
    
    
class ArticlePresentationViewSet(viewsets.ModelViewSet):
    
    serializer_class = ArticlePresentationSerializer
    queryset = tblArticlePresentation.objects.all()
    
      
class CategoryArticleViewSet(viewsets.ModelViewSet):
    
    serializer_class = CategoryArticleSerializer
    queryset = tblCategoryArticle.objects.all()
    
    
class ArticleHistoryPriceViewSet(viewsets.ModelViewSet):
    
    serializer_class = ArticleHistoryPriceSerializer
    queryset = tblArticleHistoryPrice.objects.all()
    
    
class ArticleInventoryViewSet(viewsets.ModelViewSet):
    
    serializer_class = ArticleInventorySerializer
    queryset = tblArticleInventory.objects.all()
    
    
class CompanyArticleViewSet(viewsets.ModelViewSet):
    
    serializer_class = CompanyArticleSerializer
    queryset = catCompanyArticle.objects.all()
    
    
class ProviderArticleViewSet(viewsets.ModelViewSet):
    
    serializer_class = ProviderArticleSerializer
    queryset = catProviderArticle.objects.all()
    
    
class ArticleDocumentDetailViewSet(viewsets.ModelViewSet):
    
    serializer_class = ArticleDocumentDetailSerializer
    queryset = tblArticleDocumentDetails.objects.all()
    
    


 