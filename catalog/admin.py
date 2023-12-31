from django.contrib import admin

from catalog.models import Product, Category, Blog, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'owner', 'is_published')
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Blog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_publish')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list = ('name', 'number',)
