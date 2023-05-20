from django.urls import path
# this imports all the views from the views.py
from . import views

urlpatterns = [
    # this is the home url
    path('', views.dashboard, name=''),
    # this is the single book url
]