from django.http import HttpResponse
from django.shortcuts import render
from django.template import TemplateDoesNotExist

# Create your views here.

def index(request):
    try:
        return render(request, 'shop/index.html', {})
    except TemplateDoesNotExist:
        return HttpResponse("Template not found")
    #return HttpResponse('shop index')