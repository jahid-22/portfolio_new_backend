from django.contrib import admin
from . models import Services, Category, Portfolio
# Register your models here.

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'main_title', 'sub_title']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['slug']
    prepopulated_fields = {'slug': ['name']}

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    