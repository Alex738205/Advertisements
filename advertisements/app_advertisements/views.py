from audioop import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Advertisement
from .forms import AdvertisementForm

def index(request):
    advertisement = Advertisement.objects.all()
    context = {'advertisements':advertisement}
    return render(request, "index.html", context)

def top_sellers(request):
    return render(request, "top-sellers.html")

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST,request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('index')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = { 'form': form }
    return render(request, "advertisement-post.html", context)
