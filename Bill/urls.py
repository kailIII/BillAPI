"""Bill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

from main.viewsets import CountryViewSet, CityViewSet, BDPViewSet, MailViewSet, AddressViewSet, PhoneViewSet, WebsiteViewSet, HallViewSet, AreaViewSet, AppointmentViewSet, CategorySPViewSet, CoinViewSet, CoinHistoryViewSet
from article.viewsets import BrandViewSet, ModelViewSet, ArticleViewSet, BatchViewSet, PresentationViewSet, ArticlePresentationViewSet, CategoryArticleViewSet, ArticleHistoryPriceViewSet, ArticleInventoryViewSet, CompanyArticleViewSet, ProviderArticleViewSet, ArticleDocumentDetailViewSet
from rest_framework.routers import DefaultRouter

#Router
router = DefaultRouter()
#Main Route
router.register(r'Country', CountryViewSet)
router.register(r'City', CityViewSet)
router.register(r'BDP', BDPViewSet)
router.register(r'Mail', MailViewSet)
router.register(r'Address', AddressViewSet)
router.register(r'Phone', PhoneViewSet)
router.register(r'Website', WebsiteViewSet)
router.register(r'Hall', HallViewSet)
router.register(r'Area', AreaViewSet)
router.register(r'Appointment', AppointmentViewSet)
router.register(r'CategorySP', CategorySPViewSet)
router.register(r'Coin', CoinViewSet)
router.register(r'CoinHistory', CoinHistoryViewSet)
#Article Route
router.register(r'Brand', BrandViewSet)
router.register(r'Model', ModelViewSet)
router.register(r'Article', ArticleViewSet)
router.register(r'Batch', BatchViewSet)
router.register(r'Presentation', PresentationViewSet)
router.register(r'ArticlePresentation', ArticlePresentationViewSet)
router.register(r'CategoryArticle', CategoryArticleViewSet)
router.register(r'ArticleHistoryPrice', ArticleHistoryPriceViewSet)
router.register(r'ArticleInventory', ArticleInventoryViewSet)
router.register(r'CompanyArticle', CompanyArticleViewSet)
router.register(r'ProviderArticle', ProviderArticleViewSet)
router.register(r'ArticleDocumentDetail', ArticleDocumentDetailViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
