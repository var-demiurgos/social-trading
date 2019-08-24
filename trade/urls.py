from django.urls import path
from . import views
from rest_framework import routers
from .views import AccountViewSet, Trade_ListViewSet

router = routers.DefaultRouter()
router.register(r'account', AccountViewSet)
router.register(r'trade_list', Trade_ListViewSet)

app_name='trade'
urlpatterns = [
    path('', views.index, name='index'),
    path('account', views.AccountList.as_view(), name='account'),
    path('account/create', views.AccountCreate.as_view(), name='create'),
    path('account/edit/<int:pk>', views.AccountEdit.as_view(), name='edit'),
    path('trade', views.trade, name="trade"),
    path('close', views.close, name="close")
]