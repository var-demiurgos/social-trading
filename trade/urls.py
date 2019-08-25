from django.urls import path
from . import views
from rest_framework import routers
from .views import AccountViewSet, Trade_ListViewSet
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'account', AccountViewSet)
router.register(r'trade_list', Trade_ListViewSet)

app_name='trade'
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.Login.as_view(), name='login'),
    path('account', login_required(views.AccountList.as_view()), name='account'),
    path('account/create', login_required(views.AccountCreate.as_view()), name='create'),
    path('account/edit/<int:pk>', login_required(views.AccountEdit.as_view()), name='edit'),
    path('trade', views.trade, name="trade"),
    path('close', views.close, name="close")
]