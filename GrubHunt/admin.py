from django.contrib import admin
from GrubHunt.models import FoodVendor
from GrubHunt.models import UserProfile

class FoodVendorAdmin(admin.ModelAdmin):
    list_display = ('key', 'businessName', 'description', 'address')

admin.site.register(UserProfile)
admin.site.register(FoodVendor, FoodVendorAdmin)