from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from product.models import Product

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class TagForm(forms.Form):
    tag = forms.CharField(widget=forms.TextInput(attrs={'class': ' form-control', 'placeholder': 'Add Product Type'}))
class ColorForm(forms.Form):
    color = forms.CharField(widget=forms.TextInput(attrs={'class': ' form-control', 'placeholder': 'Add Product color'}))
class SizeForm(forms.Form):
    size = forms.CharField(widget=forms.TextInput(attrs={'class': ' form-control', 'placeholder': 'Add Product size'}))
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'p_image', 'price', 'category', 'description', 'tags', 'color', 'size']