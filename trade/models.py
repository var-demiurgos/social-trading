from django.db import models

# Create your models here.
class Account(models.Model):
	account_num = models.IntegerField(blank=True)
	active      = models.CharField(max_length=10, blank=True)
	post_time   = models.DateTimeField(auto_now_add = True)

class Trade_List(models.Model):
	currency   = models.CharField(max_length=20,blank=True)
	ticket     = models.IntegerField(blank=True)
	order_type = models.BooleanField()
	lot        = models.FloatField(blank=True)
	stoploss   = models.FloatField(blank=True)
	takeprofit = models.FloatField(blank=True)
	active     = models.BooleanField()
	post_time  = models.DateTimeField(auto_now_add = True)

		
		