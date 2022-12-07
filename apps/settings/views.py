from django.shortcuts import render
from apps.settings.models import Setting
from apps.products.models import Product
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    try:
        seting = Setting.objects.latest('id')
    except:
        return HttpResponse("сурот кошшшшш админге")
    products = Product.objects.all().order_by('?')
    context = {
        'setting' : seting,
        'products' : products,
    }
    return render(request, 'index-1.html', context)




