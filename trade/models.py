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
	comment       = models.TextField(max_length=4000)

class Trade_List(models.Model):
	ticket     = models.CharField(max_length=20)
	order_type = models.CharField(max_length=20)
	lot        = models.CharField(max_length=20)
	stoploss   = models.CharField(max_length=20)
	takeprofit = models.CharField(max_length=20)
	price      = models.CharField(max_length=20)
