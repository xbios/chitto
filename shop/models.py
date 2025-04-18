from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255) # Ürün adı 
    description = models.TextField() # Ürün açıklaması
    url = models.CharField(max_length=255) # Ürün resmi
    slug = models.SlugField(max_length=255) # Ürün slug'ı
    price = models.DecimalField(max_digits=10, decimal_places=2) # Ürün fiyatı
    date = models.DateField() # Ürün tarihi
    isActive = models.BooleanField(default=True) # Ürün aktif mi?
    isUpdated = models.BooleanField(default=False) # Ürün güncellendi mi
    uploaded_image = models.FileField(blank=True,upload_to='uploads2/') # Ürün resmi yükleme alanı
    # category = models.ForeignKey('Category',blank=True,default="",on_delete=models.CASCADE) # Ürün kategorisi

    def __str__(self):
        return f"{self.name} -  {self.price} TL"


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"    
    
class Document(models.Model):
    title = models.CharField(max_length=100)
    uploaded_file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    