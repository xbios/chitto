from django import forms
from django.contrib import admin
from .models import Product, Category, Document



# class DocumentForm(forms.ModelForm):
#     class Meta:
#         model = Document
#         fields = ['title', 'uploaded_file']
       

# @admin.register(Document)
# class DocumentAdmin(admin.ModelAdmin):
#     form = DocumentForm
#     list_display = ('title', 'uploaded_at')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):        
    list_display = ('name', 'date', 'price', 'isActive', 'isUpdated') 
    list_display_links = ('name', 'date')   
    readonly_fields = ('slug',)
    list_filter = ('name','isActive', 'isUpdated')   
    list_editable = ('isActive',)
    search_fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('name', 'slug')
    list_display_links = ('name', 'slug')
    search_fields = ('name',)


    
