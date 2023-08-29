from django.urls import path
from .views import advertisement_details, index, top_sellers, advertisement_post

urlpatterns = [
    path('', index, name = "index"),
    path('top-sellers/', top_sellers, name = "top-sellers"),
    path('advertisement-post/', advertisement_post, name = "adv-post"),
    path('advertisement/<int:pk>', advertisement_details, name = "adv-details"),
]
