from django.db import models

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
	last_login   = models.DateTimeField(blank=True)
	comment      = models.TextField(max_length=4000)

class Trade_List(models.Model):
	order_type = models.IntegerField()
	lot        = models.FloatField()
	stoploss   = models.TextField(max_length=100)
	takeprofit = models.CharField(max_length=100)
	open_price = models.CharField(max_length=100)
	ticket     = models.IntegerField()
