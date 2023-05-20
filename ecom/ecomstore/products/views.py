from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Product
from categorys.models import Category

# Create your views here.
# this is a view for listing all the product


def dashboard(request):
    # retrieving all the product from the database
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/home.html', context)

# this is a view for listing a single product
def product_detail(request, id):
    # querying a particular product by its id
    product = Product.objects.get(pk=id)
    context = {'product': product}
    return render(request, 'products/product-detail.html', context)

# this is a view for editing the book's info
def add_product(request):
    categorys = Category.objects.all()
    context = {'categorys': categorys}
    # checking if the method is POST
    if request.method == 'POST':
        # getting all the data from the POST request
        data = request.POST
        # getting the image
        image = request.FILES.get('image-file')
        # creating and saving the book
        product = Product.objects.create(
           title = data['title'],
           name = data['name'],
           description = data['description'],
           tags = data['tags'],
           category = Category.objects.get(id=data['category']),
           image = image
        )
        # going to the home page
        return redirect('product-list')
    return render(request, 'products/add_product.html', context)

# this is a view for editing the product's info
def edit_product(request,id):
    categorys = Category.objects.all()
    # getting the product to be updated
    product = Product.objects.get(pk=id)
    # checking if the request is POST
    if request.method == 'POST':
        # getting all the data from the POST request
        data = request.POST
        # getting the image
        image = request.FILES.get('image-file')
        # creating and saving the book
        product = Product.objects.update_or_create(
           title = data['title'],
           name = data['name'],
           description = data['description'],
           tags = data['tags'],
           category = Category.objects.get(id=data['category']),
           image = image
        )
        # going to the home page
        return redirect('product-list')
    context = {'product': product, 'categorys': categorys}
    return render(request, 'products/update-product.html', context)

# this is a view for deleting a book,it will take id as an argument
def delete_product(request, id):
    return HttpResponse('Delete Book')
