from django.urls import path

from .views import ads_list, category_list, create_ad


urlpatterns = [
    path("", ads_list, name="index"),
    path("category", category_list, name="category"),
    path("create", create_ad, name="create"),
]