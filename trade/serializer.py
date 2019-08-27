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

    class Meta:
        model = Account
        fields = ('account_num', 'active')

    def update(self, validated_data):
    	print("AC:"+validated_data['account_num'])
        account = Account.objects.get(account_num=validated_data['account_num']).updata(last_login=timezone.now)
        account.save()
        return user

class Trade_ListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Trade_List
    fields = ('ticket','order_type','lot','stoploss','takeprofit','open_price')