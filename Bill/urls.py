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

from main.viewsets import UserViewSet, CountryViewSet, CityViewSet, BDPViewSet, MailViewSet, AddressViewSet, PhoneViewSet, WebsiteViewSet, HallViewSet, AreaViewSet, AppointmentViewSet, CategorySPViewSet, CoinViewSet, CoinHistoryViewSet
from article.viewsets import BrandViewSet, ModelViewSet, ArticleViewSet, BatchViewSet, PresentationViewSet, ArticlePresentationViewSet, CategoryArticleViewSet, ArticleHistoryPriceViewSet, ArticleInventoryViewSet, CompanyArticleViewSet, ProviderArticleViewSet, ArticleDocumentDetailViewSet
from bank.viewsets import BankViewSet, BankControlViewSet, BankControlDetailViewSet, BankControlAdjustViewSet
from client.viewsets import KindClientViewSet, ClientViewSet, BusinessContactViewSet 
from company.viewsets import CompanyViewSet, CompanyHallsViewSet, EmployeeViewSet, EmployeeHistoryViewSet, MembershipViewSet, DocumentViewSet, DocumentDetailCredictViewSet 
from order.viewsets import OrderViewSet
from provider.viewsets import ProviderViewSet, ProviderHallsViewSet
from purchase.viewsets import PurchaseViewSet
from sale.viewsets import SaleViewSet
from service.viewsets import KindServiceViewSet, ServiceViewSet, CategoryServicesViewSet, ServicesHistoryPriceViewSet, ServiceDocumentDetailsViewSet, ServiceCostViewSet, ServiceCostDetailViewSet, ServiceManageViewSet, ScheduleDateViewSet, ScheduleDateDetailViewSet, ProviderServiceViewSet, CompanyServiceViewSet 
from rest_framework.routers import DefaultRouter

#Router
router = DefaultRouter()
#Main Route
router.register(r'User', UserViewSet)
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
#Bank Route
router.register(r'Bank', BankViewSet)
router.register(r'BankControl', BankControlViewSet)
router.register(r'BankControlDetail', BankControlDetailViewSet)
router.register(r'BankControlAdjust', BankControlAdjustViewSet)
#Client Route
router.register(r'KindClient', KindClientViewSet)
router.register(r'Client', ClientViewSet)
router.register(r'BusinessContact', BusinessContactViewSet)
#Company Route
router.register(r'Company', CompanyViewSet)
router.register(r'CompanyHalls', CompanyHallsViewSet)
router.register(r'Employee', EmployeeViewSet)
router.register(r'EmployeeHistory', EmployeeHistoryViewSet)
router.register(r'Membership', MembershipViewSet)
router.register(r'Document', DocumentViewSet)
router.register(r'DocumentDetailCredict', DocumentDetailCredictViewSet)
#Order Route
router.register(r'Order', OrderViewSet)
#Provider Route
router.register(r'Provider', ProviderViewSet)
router.register(r'ProviderHalls', ProviderHallsViewSet)
#Purchase Route
router.register(r'Purchase', PurchaseViewSet)
#Sale Route
router.register(r'Sale', SaleViewSet)
#Service Route
router.register(r'KindService', KindServiceViewSet)
router.register(r'Service', ServiceViewSet)
router.register(r'CategoryServices', CategoryServicesViewSet)
router.register(r'ServicesHistoryPrice', ServicesHistoryPriceViewSet)
router.register(r'ServiceDocumentDetails', ServiceDocumentDetailsViewSet)
router.register(r'ServiceCost', ServiceCostViewSet)
router.register(r'ServiceCostDetail', ServiceCostDetailViewSet)
router.register(r'ServiceManage', ServiceManageViewSet)
router.register(r'ScheduleDate', ScheduleDateViewSet)
router.register(r'ScheduleDateDetail', ScheduleDateDetailViewSet)
router.register(r'ProviderService', ProviderServiceViewSet)
router.register(r'CompanyServiceView', CompanyServiceViewSet)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
