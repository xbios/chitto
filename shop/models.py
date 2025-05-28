from django.db import models
from django.utils.text import slugify
from django.utils.html import mark_safe

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args,kwargs)

    def __str__(self):
        return f"{self.name}"  


class Product(models.Model):
    category = models.ForeignKey(Category,null=True,default=1,on_delete=models.SET_NULL) 
    name = models.CharField(max_length=255) 
    description = models.TextField() 
    color = models.CharField(blank=True,max_length=50)
    size = models.CharField(blank=True,max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    isActive = models.BooleanField(default=True) 
    isUpdated = models.BooleanField(default=False) 
    date = models.DateField(auto_now=True) 
    url = models.CharField(max_length=255) 
    slug = models.SlugField(default="",blank=True, editable=False, null=False, unique=True, db_index=True) 
    uploaded_image = models.FileField(blank=True,upload_to='uploads2/') 
    uploaded_image2 = models.FileField(blank=True,upload_to='uploads2/') 
    uploaded_image3 = models.FileField(blank=True,upload_to='uploads2/') 

    def image_tag(self):
        if self.uploaded_image:  # Eğer bir resim yüklü ise
            return mark_safe(f'<img src="/media/{self.uploaded_image}" width="125" height="125" />')
        return "Resim Yok"  # Eğer resim yoksa gösterilecek metin
    image_tag.short_description = 'Image'  # Admin arayüzünde etiket adını belirler

    def image_tag2(self):
        if self.uploaded_image2:  # Eğer bir resim yüklü ise
            return mark_safe(f'<img src="/media/{self.uploaded_image2}" width="125" height="125" />')
        return "Resim Yok"  # Eğer resim yoksa gösterilecek metin
    image_tag2.short_description = 'Image 2' 

    def image_tag3(self):
        if self.uploaded_image3:  # Eğer bir resim yüklü ise
            return mark_safe(f'<img src="/media/{self.uploaded_image3}" width="125" height="125" />')
        return "Resim Yok"  # Eğer resim yoksa gösterilecek metin
    image_tag3.short_description = 'Image 3'  
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args,kwargs)

    def __str__(self):
        return f"{self.name} -  {self.price} TL"


  
    
class Document(models.Model):
    title = models.CharField(max_length=100)
    uploaded_file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    