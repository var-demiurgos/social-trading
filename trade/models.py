from django.db import models
from django.utils import timezone
# Create your models here.
class Account(models.Model):
	ACTIVE = (
		('A', '有効'), 
		('B', '無効'),
		('C', '退会'),
	)
	account_id   = models.IntegerField()
	account_pass = models.CharField(max_length=100)
	account_num  = models.IntegerField(blank=True)
	active       = models.CharField(max_length=10, choices=ACTIVE)
	post_time    = models.DateTimeField(auto_now_add = True)
	last_login   = models.DateTimeField(default=timezone.now)
	comment      = models.TextField(max_length=4000)

class Trade_List(models.Model):
	ticket     = models.IntegerField()
	order_type = models.IntegerField()
	lot        = models.FloatField()
	stoploss   = models.TextField(max_length=100)
	takeprofit = models.CharField(max_length=100)
	open_price = models.CharField(max_length=100)

class Test(models.Model):
	ticket     = models.IntegerField()
	order_type = models.IntegerField()
	lot        = models.FloatField()
	stoploss   = models.TextField(max_length=100)
	takeprofit = models.CharField(max_length=100)
	open_price = models.CharField(max_length=100)
	pair       = models.CharField(max_length=30)