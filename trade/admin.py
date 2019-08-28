from django.contrib import admin
from .models import Account, Trade_List, Test

# Register your models here.

admin.site.register(Account)
admin.site.register(Trade_List)
admin.site.register(Test)