from django.db import models
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255) 
    description = models.TextField() 
    url = models.CharField(max_length=255) 
    slug = models.SlugField(default="",blank=True, editable=False, null=False, unique=True, db_index=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    date = models.DateField() 
    isActive = models.BooleanField(default=True) 
    isUpdated = models.BooleanField(default=False) 
    uploaded_image = models.FileField(blank=True,upload_to='uploads2/') 
    # category = models.ForeignKey('Category',blank=True,default="",on_delete=models.CASCADE) 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args,kwargs)

    def __str__(self):
        return f"{self.name} -  {self.price} TL"


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args,kwargs)

    def __str__(self):
        return f"{self.name}"    
    
class Document(models.Model):
    title = models.CharField(max_length=100)
    uploaded_file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    