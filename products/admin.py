from django.contrib import admin

from utils.admin import BaseModelAdmin
from .models import Product, Batch


class ProductAdmin(BaseModelAdmin):
    list_display = ['id', 'created_on', 'updated_on', 'name']
    readonly_fields = ['id', 'created_on', 'updated_on']


admin.site.register(Product, ProductAdmin)


class BatchAdmin(BaseModelAdmin):
    list_display = ['id', 'created_on', 'updated_on', 'product', 'amount', 'expires_on']
    readonly_fields = ['id', 'created_on', 'updated_on']
    autocomplete_fields = ['product']


admin.site.register(Batch, BatchAdmin)
