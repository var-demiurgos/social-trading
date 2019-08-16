from django.db import models

# Create your models here.
class Account(models.Model):
	ACTIVE = (
		('A', '有効'), 
		('B', '無効'),
		('C', '退会'),
	)
	account_num = models.IntegerField(blank=True)
	active     = models.CharField(max_length=10, choices=ACTIVE)
	post_time   = models.DateTimeField(auto_now_add = True)
	last_login  = models.DateTimeField(blank=True)

class Trade_List(models.Model):
	ticket     = models.IntegerField(blank=True)
	order_type = models.IntegerField()
	lot        = models.FloatField(blank=True)
	stoploss   = models.FloatField(blank=True)
	takeprofit = models.FloatField(blank=True)
	active     = models.CharField(max_length=10)
	post_time  = models.DateTimeField(auto_now_add = True)
