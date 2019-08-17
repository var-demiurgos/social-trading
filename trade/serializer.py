from rest_framework import serializers

from .models import Account, Trade_List

class AccountSerializer(serializers.ModelSerializer):
  class Meta:
    model = Account
    fields = ('account_num', 'active','post_time')


class Trade_ListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Trade_List
    fields = ('ticket','order_type','lot','stoploss','takeprofit','post_time','active')