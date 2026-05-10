from django.contrib import admin
from .models import Organization, Category, Product


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'category', 'organization', 'price', 'quantity', 'min_limit')
    search_fields = ('name', 'sku')
    list_editable = ('quantity', 'price')