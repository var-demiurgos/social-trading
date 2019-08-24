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
	data = Trade_List.objects.all()
	params = {'data':data}
	return render(request, 'trade/index.html',params)

def account(request):
	account = Account.objects.all()
	context = {"account": account}
	return render(request, 'trade/account.html', context)

class Account(generic.ListView, ModelFormMixin):
    model = Account
    fields = '__all__'
    success_url = reverse_lazy('app:list_and_create')  # このビュー自身!
    template_name = 'trade/account.html'
 
 
    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)
 
    def post(self, request, *args, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

def close(request):
	ticket = request.GET.get("ticket")
	trade  = Trade_List.objects.get(ticket=ticket)
	trade.delete()
	return render(request, 'trade/account/html')

def trade(request):
	ticket     = request.GET.get("ticket")
	order_type = request.GET.get("order_type")
	lot        = request.GET.get("lot")
	takeprofit = request.GET.get("takeprofit")
	stoploss   = request.GET.get("stoploss")
	open_price = request.GET.get("open_price")

	trade      = Trade_List.objects.update_or_create(ticket=ticket, defaults={"order_type":order_type, "lot":lot, "stoploss":stoploss, "takeprofit":takeprofit, "open_price":open_price})
	return render(request, 'trade/account/html')
