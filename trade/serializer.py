from rest_framework import serializers

from .models import Account, Trade_List

class AccountSerializer(serializers.ModelSerializer):
  class Meta:
    model = Account
    fields = ('account_id', 'account_pass', 'account_num', 'active', 'post_time', 'last_login', 'comment')


class Trade_ListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Trade_List
    fields = ('ticket','order_type','lot','stoploss','takeprofit','price')