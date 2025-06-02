from django import forms
from .models import Item, Categoria, Autor, Editora

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'categoria', 'autor', 'editora']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['name']
        
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['name']

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['name']