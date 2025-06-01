from django import forms
from .models import Item, Categoria, Autor

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'categoria', 'autor']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['name']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['name']
