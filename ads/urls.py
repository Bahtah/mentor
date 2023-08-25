from django.urls import path

from .views import AdsListView, AdsDetailView, AdsUpdateView, AdsDeleteView, AdsCreateView


urlpatterns = [
    path("", AdsListView.as_view(), name="index"),
    path("create", AdsCreateView.as_view(), name="create"),
    path("update_ad/<int:pk>/", AdsUpdateView.as_view(), name="update_ad"),
    path("<int:pk>/", AdsDetailView.as_view(), name="retrieve_ad"),
    path("delete/<int:pk>/", AdsDeleteView.as_view(), name="delete_ad"),
]