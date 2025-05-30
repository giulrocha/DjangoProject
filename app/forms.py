from django import forms
from .models import Item, Categoria, Editora

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'categoria']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['name']


class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['name']
