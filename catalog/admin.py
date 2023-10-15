from django.contrib import admin
from .models import Category, Product, Version

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'purchase_price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'number', 'name', 'is_active',)
    list_filter = ('is_active', 'product')
