from django.contrib import admin
from .models import items
# Register your models here.
from django.contrib import admin


admin.site.register(items)
# class PostModelAdmin(admin.ModelAdmin):
#     list_display = ["purchased_date", "item", "item_category", "quantity", "price"]
