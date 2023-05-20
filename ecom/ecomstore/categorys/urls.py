from django.urls import path
# this imports all the views from the views.py
from . import views

urlpatterns = [
    # this is the home url
    path('', views.home, name='home'),
    # this is the single book url
    path('category-detail/<str:id>/',
         views.category_detail, name='category-detail'),
    # this is the add book url
    path('add-category/', views.add_category, name='add-category'),
    # this is the edit book url
    path('edit-category/<str:id>/', views.edit_category, name='edit-category'),
    # this is the delete book url
    path('delete-category/<str:id>/',
         views.delete_category, name='delete-category'),
]
