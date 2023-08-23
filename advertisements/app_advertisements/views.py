from audioop import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required

def index(request):
    advertisement = Advertisement.objects.all()
    context = { 'advertisements':advertisement }
    return render(request, "app_advertisements/index.html", context)

def top_sellers(request):
    return render(request, "app_advertisements/top-sellers.html")

@login_required(login_url=reverse_lazy('login'))
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
    return render(request, "app_advertisements/advertisement-post.html", context)
