from django import forms
from django.contrib import admin
from .models import Product, Category, Document

admin.site.site_header = "Chitto Shop Admin"
admin.site.site_title = "Chitto Shop Admin Portal"

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
    readonly_fields = ('image_tag', 'image_tag2','image_tag3','slug','url')
    list_filter = ('category','isActive', 'isUpdated')
    list_editable = ('isActive',)
    search_fields = ('name', 'description')
    fieldsets = (
        ('ürün Bilgileri', {
            'classes': ('wide',),  # 'wide' sınıfı alanları genişçe yayar
            'fields': ('isActive','category','name', 'description','color','size','price'),  # Yan yana göstermek istediğiniz alanları buraya ekleyin
        }),
        ('Resim 1', {
            'classes': ('wide',),  # 'wide' sınıfı alanları genişçe yayar
            'fields': ('uploaded_image', 'image_tag'),  # Yan yana göstermek istediğiniz alanları buraya ekleyin
        }),
        ('Resim 2', {
            'classes': ('wide'),  
            'fields': ('uploaded_image2','image_tag2'),
        }),
        ('Resim 3', {
            'classes': ('wide'),  
            'fields': ('uploaded_image3','image_tag3'),
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('name', 'slug')
    list_display_links = ('name', 'slug')
    search_fields = ('name',)


    
