from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from rest_framework import viewsets, generics
from .models import Account, Trade_List, Test
from .serializer import AccountSerializer, Trade_ListSerializer, AccountFilter, TestSerializer
from .forms import AccountForm
from django.contrib.auth.views import LoginView
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
	return render(request, 'trade/index.html')

class Login(LoginView):
	template_name = 'trade/login.html'

class TradeList(ListView):
    model = Trade_List
    template_name = 'trade/trade.html'

class AccountList(LoginRequiredMixin, ListView):
    model = Account
    template_name = 'trade/account.html'

class AccountEdit(LoginRequiredMixin, UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'trade/account_form.html'
    success_url = "/trade/account/list"

class AccountCreate(LoginRequiredMixin, CreateView):
    model = Account
    form_class = AccountForm
    template_name = 'trade/account_form.html'
    success_url = "list"

class AccountDelete(LoginRequiredMixin, DeleteView):
	model = Account
	success_url = "/trade/account/list"

#MT4からのアクセス用

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

def last_login(request):
	account_num = request.GET.get("account_num")
	account  = Account.objects.get(account_num=account_num)
	account.last_login = timezone.now()
	account.save()
	return HttpResponse("ok.")

class AccountViewSet(viewsets.ModelViewSet):
	queryset         = Account.objects.all()
	serializer_class = AccountSerializer

class AccountFilterViewSet(viewsets.ModelViewSet):
	queryset         = Account.objects.all()
	serializer_class = AccountSerializer
	filter_class     = AccountFilter

class Trade_ListViewSet(viewsets.ModelViewSet):
	queryset         = Trade_List.objects.all()
	serializer_class = Trade_ListSerializer





class TestViewSet(viewsets.ModelViewSet):
	queryset         = Test.objects.all()
	serializer_class = TestSerializer


# class TestFilterViewSet(viewsets.ModelViewSet):
# 	queryset         = Test.objects.all()
# 	serializer_class = TestSerializer
# 	filter_class     = TestFilter