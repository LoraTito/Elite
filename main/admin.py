from django.contrib import admin

from main.models import HorseForSale
from main.models import ImageGallery

class HorseForSaleAdmin(admin.ModelAdmin):
    list_display = ['date_of_listing', 'name', 'breed', 'price']

admin.site.register(HorseForSale, HorseForSaleAdmin)

class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ['image']

admin.site.register(ImageGallery, ImageGalleryAdmin)

