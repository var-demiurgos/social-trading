from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect,render_to_response
from django.views import generic
from django.template import RequestContext
from django.views.generic.edit import ModelFormMixin
from django.views.generic import CreateView, UpdateView, ListView
import django_filters
from rest_framework import viewsets, filters
from .models import Account, Trade_List
from .serializer import AccountSerializer, Trade_ListSerializer

class AccountViewSet(viewsets.ModelViewSet):
	queryset         = Account.objects.all()
	serializer_class = AccountSerializer

class Trade_ListViewSet(viewsets.ModelViewSet):
	queryset         = Trade_List.objects.all()
	serializer_class = Trade_ListSerializer

def index(request):
	return render(request, 'trade/index.html')

def account(request):
	return render(request, 'trade/account/html')

def trade(request):
	ticket     = request.GET.get("ticket")
	order_type = request.GET.get("order_type")
	lot        = request.GET.get("lot")
	takeprofit = request.GET.get("takeprofit")
	stoploss   = request.GET.get("stoploss")
	price      = request.GET.get("price")
	print(price)
	trade      = Trade_List.objects.create(ticket=ticket, order_type=order_type, lot=lot, stoploss=stoploss, takeprofit=takeprofit, price=price)
	return render(request, 'trade/account/html')
