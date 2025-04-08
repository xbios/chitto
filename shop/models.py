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

    def __str__(self):
        return f"{self.name} -  {self.price} TL"


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"    