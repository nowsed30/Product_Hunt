from django.contrib import admin
from .models import Product

class product_detail(admin.ModelAdmin):
    list_display=['title','pub_date','body','url']

admin.site.register(Product)
