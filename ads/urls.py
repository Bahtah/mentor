from django.urls import path

from .views import ads_list, category_list, create_ad, update_ad


urlpatterns = [
    path("", ads_list, name="index"),
    path("category", category_list, name="category"),
    path("create", create_ad, name="create"),
    path("update_ad/<int:pk>/", update_ad, name="update_ad"),
]