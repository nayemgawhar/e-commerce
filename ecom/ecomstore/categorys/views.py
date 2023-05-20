from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import EditCategoryForm
from .models import Category

# Create your views here.
# this is a view for listing all the category


def home(request):
    # retrieving all the category from the database
    categorys = Category.objects.all()
    context = {'categorys': categorys}
    return render(request, 'categorys/home.html', context)

# this is a view for listing a single book,it will take id as an argument


def category_detail(request, id):
    # querying a particular category by its id
    category = Category.objects.get(pk=id)
    context = {'category': category}
    return render(request, 'categorys/category-detail.html', context)

# this is a list for adding a book


def add_category(request):
    # checking if the method is POST
    if request.method == 'POST':
        # getting all the data from the POST request
        data = request.POST
        # creating and saving the book
        category = Category.objects.create(
            name=data['name'],
            tags=data['tags'],
        )
        # going to the home page
        return redirect('home')
    return render(request, 'categorys/add_category.html')

# this is a view for editing the category's info


def edit_category(request, id):
    # getting the category to be updated
    category = Category.objects.get(pk=id)
    # populating the form with the category's information
    form = EditCategoryForm(instance=category)
    # checking if the request is POST
    if request.method == 'POST':
        # filling the form with all the request data 
        form = EditCategoryForm(request.POST, request.FILES, instance=category)
        # checking if the form's data is valid
        if form.is_valid():
            # saving the data to the database
            form.save()
            # redirecting to the home page
            return redirect('home')
    context = {'form': form}
    return render(request, 'categorys/update-category.html', context)

# this is a view for deleting a category,it will take id as an argument

def delete_category(request, id):
    # getting the category to be deleted
    category = Category.objects.get(pk=id)
    # checking if the method is POST
    if request.method == 'POST':
        # delete the category
        category.delete()
        # return to home after a success delete
        return redirect('home')
    context = {'category': category}
    return render(request, 'categorys/delete-category.html', context)
