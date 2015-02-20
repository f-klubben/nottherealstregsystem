from django.contrib import admin

from .models import Listing, PointOfSale, Product, Tag

admin.site.register(Product)
admin.site.register(PointOfSale)
admin.site.register(Listing)
admin.site.register(Tag)
