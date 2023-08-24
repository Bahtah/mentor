from django.contrib import admin

from .models import Ads,Category,SubCategory

class AdsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "type")
    list_display_links = ("id", "title")
    list_editable = ("type", )
    list_filter = ("type", )
    search_fields = ("title", "price")

admin.site.register(Ads, AdsAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
