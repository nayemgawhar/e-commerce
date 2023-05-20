from .models import Category
from django.forms import ModelForm
from django import forms

# declaring the ModelForm
class EditCategoryForm(ModelForm):
    
    class Meta:
        # the Model from which the form will inherit from
        model = Category
        # the fields we want from the Model
        fields = '__all__'
        # styling the form with bootstrap classes
        widgets = {
             'name': forms.TextInput(attrs={'class': 'form-control'}),
             'tags': forms.TextInput(attrs={'class': 'form-control'}),
        }
