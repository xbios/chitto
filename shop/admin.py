from django.contrib import admin
from .models import Product, Category

# Register your models here.
admin.site.register(Product)
admin.site.site_header = "Chitto Admin Paneli"
admin.site.site_title = "Chitto Admin Paneli"
admin.site.index_title = "Chitto Admin Paneli" # Admin panelinin başlığı


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass