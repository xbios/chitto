from datetime import date, datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import TemplateDoesNotExist

# Create your views here.

db = { 
    "urunliste" : [
        {             
            "name": "javascript kursu", 
            "description": "javascript kurs açıklaması", 
            "url": "1.jpg",
            "slug": "javascript-kursu",
            "price": 100,
            "date": datetime.now(),
            "isActive": True,
            "isUpdated": False
        },
        {             
            "name": "python kursu", 
            "description": "python kurs açıklaması", 
            "url": "2.jpg",
            "slug": "python-kursu",
            "price": 110,
            "date": date(2025, 9, 10),
            "isActive": True,
            "isUpdated": False
        },
        {             
            "name": "web geliştirme kursu", 
            "description": "web geliştirme kurs açıklaması", 
            "url": "3.jpg",
            "slug": "web-gelistirme-kursu",
            "price": 120,
            "date": date(2025, 8, 10),
            "isActive": True,
            "isUpdated": True
        },
             {       "name": "javascript kursu", 
            "description": "javascript kurs açıklaması", 
            "url": "1.jpg",
            "slug": "javascript-kursu",
            "price": 100,
            "date": datetime.now(),
            "isActive": True,
            "isUpdated": False
        },
        {             
            "name": "python kursu", 
            "description": "python kurs açıklaması", 
            "url": "2.jpg",
            "slug": "python-kursu",
            "price": 110,
            "date": date(2025, 9, 10),
            "isActive": True,
            "isUpdated": False
        },
        {             
            "name": "web geliştirme kursu", 
            "description": "web geliştirme kurs açıklaması", 
            "url": "3.jpg",
            "slug": "web-gelistirme-kursu",
            "price": 120,
            "date": date(2025, 8, 10),
            "isActive": True,
            "isUpdated": True
        }
    ],
 
}

def index(request):
    products = db["urunliste"]
    try:
        return render(request, 'shop/index.html',{         
        'products': products,
        })
    except TemplateDoesNotExist:
        return HttpResponse("Template not found")
    #return HttpResponse('shop index')