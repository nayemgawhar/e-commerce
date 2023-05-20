from django.http import HttpResponse
from django.shortcuts import redirect, render
from products.models import Product
from categorys.models import Category

# Create your views here.

def dashboard(request):
    # retrieving all the product from the database
    products = Product.objects.count()
    categorys = Category.objects.count()
    context = {'products': products,'categorys': categorys}
    
    return render(request, 'welcome.html', context)
