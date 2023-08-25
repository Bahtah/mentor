from typing import Any, Dict
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime, date, time
from django.views import View
from django.views.generic import  ListView, DetailView, UpdateView, DeleteView, CreateView

from users.models import User

from .models import Ads, Category
from .forms import AdForm


class AdsListView(ListView):
    template_name = 'index.html'
    queryset = Ads.objects.all()
    context_object_name = 'all_ads'
    
class AdsDetailView(DetailView):
    template_name = 'retrieve_ad.html'
    queryset = Ads.objects.all()
    context_object_name = 'ad'
    
class AdsUpdateView(UpdateView):
    template_name = 'update_ad.html'
    queryset = Ads.objects.all()
    form_class = AdForm
    
    def get_success_url(self) -> str:
        return reverse('index')

class AdsDeleteView(DeleteView):
    queryset = Ads.objects.all()
    template_name = 'delete_ad.html'
    success_url = reverse_lazy('index')
    
class AdsCreateView(CreateView):
    queryset = Ads.objects.all()
    template_name = 'create_ad.html'
    form_class = AdForm
    
    def get_success_url(self):
        return reverse('index')