from django.urls import path
# this imports all the views from the views.py
from . import views

urlpatterns = [
    # this is the home url
    path('', views.dashboard, name='product-list'),
    # this is the single book url
    path('product-detail/<str:id>/',
         views.product_detail, name='product-detail'),
    # this is the add book url
    path('add-product/', views.add_product, name='add-product'),
    # # this is the edit book url
    path('edit-product/<str:id>/', views.edit_product, name='edit-product'),
    # # this is the delete book url
    path('delete-product/<str:id>/',
         views.delete_product, name='delete-product'),
]