from django import forms
from django.contrib import admin
from .models import Product, Category, Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'uploaded_file']


# Register your models here.
admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):    
    list_display = ('title', 'uploaded_at')    
    
admin.site.site_header = "Chitto Admin Paneli"
admin.site.site_title = "Chitto Admin Paneli"
admin.site.index_title = "Chitto Admin Paneli" # Admin panelinin başlığı


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    form = DocumentForm
    list_display = ('title', 'uploaded_at')
    