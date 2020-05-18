from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from product.models import Product, Tag, Color, Size

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['color']

class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = ['size']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


