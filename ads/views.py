from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime, date, time
from django.views import View
from django.views.generic import  ListView

from users.models import User

from .models import Ads, Category
from .forms import AdForm


def category_list(request):
    all_categories = Category.objects.all()
    context = {
        "all_categories": all_categories
    }
    return render(request, 'category.html', context=context)

def ads_list(request):
    all_ads = Ads.objects.all()
    # all_ads = Ads.objects.filter(created_at__day__lt=24)
    # all_ads = Ads.objects.filter(title__icontains="test")
    # all_ads = Ads.objects.filter(owner__isnull=True)
    # all_ads = Ads.objects.filter(created_at__year=2023) & Ads.objects.filter(description__contains="b")
    # admin = User.objects.get(username="mentor")
    # all_ads = Ads.objects.filter(owner=admin)
    # all_ads = Ads.objects.filter(price__in=[200, 3000, 343, 2500])
    context = {
        "all_ads": all_ads
    }
    return render(request, 'index.html', context=context)
    
            

def create_ad(request):
    if request.method == "POST":
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form_of_ad = AdForm()
    return render(request, "create_ad.html", {'form_of_ad': form_of_ad})

def update_ad(request, pk):
    ad = get_object_or_404(Ads, id=pk)
    
    if request.method == "POST":
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, "update_ad.html", {"form_of_ad": form_of_ad})
    else:
        form_of_ad=AdForm(instance=ad)
        return render(request, "update_ad.html", {"form_of_ad": form_of_ad}) 
    
    
def retrieve_ad(request, pk):
    ad = Ads.objects.get(id=pk)
    context = {
        "ad": ad
    }
    return render(request, "retrieve_ad.html", context=context)


def delete_ad(request, pk):
    ad = Ads.objects.get(id=pk)
    ad.delete()
    messages.success(request, "Обьект успешно удален!!!")
    return redirect('index')
    