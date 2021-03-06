from django.urls import path
from . import views
from rest_framework import routers
from .views import AccountViewSet, Trade_ListViewSet, AccountFilterViewSet,TestViewSet, TestFilterViewSet
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'account', AccountViewSet)
router.register(r'search_account', AccountFilterViewSet)
router.register(r'trade_list', Trade_ListViewSet)
router.register(r'tests', TestViewSet)
router.register(r'search_tests', TestFilterViewSet)

app_name='trade'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.Login.as_view(), name='login'),
    path('account/list', views.AccountList.as_view(), name='account'),
    path('trade/list', views.TradeList.as_view(), name='trades'),
    path('account/create',views.AccountCreate.as_view(), name='create'),
    path('account/edit/<int:pk>', views.AccountEdit.as_view(), name='edit'),
    path('account/delete/<int:pk>', views.AccountDelete.as_view(), name='delete'),
    path('trade', views.trade, name="trade"),
    path('close', views.close, name="close"),
    path('last', views.last_login, name="last"),
    path('testtrade', views.testtrade, name="testtrade"),
    path('testclose', views.testclose, name="testclose"),
    path('trade/lists', views.testTradeList.as_view(), name='testtrades'),
    path('trade/lists/<str:pair>', views.testpairTradeList.as_view(), name='tradepair'),

]