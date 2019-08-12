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
    path('account', views.account, name='account'),
    path('<int:pk>/<str:active>', views.active, name="active")
]