from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.template import RequestContext
from django.views.generic.edit import ModelFormMixin
from django.views.generic import CreateView, UpdateView, ListView

def home(request):
	return render(request, 'trade/index.html')
