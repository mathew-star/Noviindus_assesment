from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    """
    Form for adding and editing products.
    """
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'clear_checkbox_label': ''}),
        }
