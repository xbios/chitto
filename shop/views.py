from datetime import date, datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import TemplateDoesNotExist

# Create your views here.

db = { 
    "urunliste" : [
        {             
            "name": "KRT Chitto Açık Elekli Kedi Tuvaleti", 
            "description": "KRT Chitto Açık Elekli Kedi Tuvaleti Turuncu", 
            "url": "tur1.png",
            "slug": "javascript-kursu",
            "price": 100,
            "date": datetime.now(),
            "isActive": True,
            "isUpdated": False
        },
        {             
            "name": "python kursu", 
            "description": "python kurs açıklaması", 
            "url": "tuv1.jpeg",
            "slug": "python-kursu",
            "price": 110,
            "date": date(2025, 9, 10),
            "isActive": True,
            "isUpdated": False
        },
        {             
            "name": "web geliştirme kursu", 
            "description": "web geliştirme kurs açıklaması", 
            "url": "ev1.jpeg",
            "slug": "web-gelistirme-kursu",
            "price": 120,
            "date": date(2025, 8, 10),
            "isActive": True,
            "isUpdated": True
        },
             {       
            "name": "javascript kursu", 
            "description": "javascript kurs açıklaması", 
            "url": "ev2.jpeg",
            "slug": "javascript-kursu",
            "price": 100,
            "date": datetime.now(),
            "isActive": True,
            "isUpdated": False
        },
        {             
            "name": "python kursu", 
            "description": "python kurs açıklaması", 
            "url": "ev3.jpeg",
            "slug": "python-kursu",
            "price": 110,
            "date": date(2025, 9, 10),
            "isActive": True,
            "isUpdated": False
        },
        {             
            "name": "web geliştirme kursu", 
            "description": "web geliştirme kurs açıklaması", 
            "url": "ev4.jpeg",
            "slug": "web-gelistirme-kursu",
            "price": 120,
            "date": date(2025, 8, 10),
            "isActive": True,
            "isUpdated": True
        },
        {             
            "name": "python kursu", 
            "description": "python kurs açıklaması", 
            "url": "paspas1.jpeg",
            "slug": "python-kursu",
            "price": 110,
            "date": date(2025, 9, 10),
            "isActive": True,
            "isUpdated": False
        },
        {             
            "name": "web geliştirme kursu", 
            "description": "web geliştirme kurs açıklaması", 
            "url": "paspas2.jpeg",
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