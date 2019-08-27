from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import Account, Trade_List
from django.utils import timezone

class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ('account_id', 'account_pass', 'account_num', 'active', 'post_time', 'last_login', 'comment')

class AccountFilter(filters.FilterSet):
	account_num = filters.NumberFilter(lookup_expr='exact')
	active = filters.CharFilter(lookup_expr='exact')
	print("AC:"+account_num)

	class Meta:
		model = Account
		fields = ('account_num', 'active')

class Trade_ListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Trade_List
		fields = ('ticket','order_type','lot','stoploss','takeprofit','open_price')