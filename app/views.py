from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Categoria, Editora
from .forms import ItemForm, CategoriaForm, EditoraForm

##ITEM

def item_list(request):
    items = Item.objects.all()
    return render(request, 'app/item_list.html', {'items': items})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'app/item_form.html', {'form': form})

def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'app/item_form.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'app/item_confirm_delete.html', {'item': item})


## Categoria [feature/thiago]

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'app/categoria_list.html', {'categorias': categorias})

def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'app/categoria_form.html', {'form': form})

def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'app/categoria_form.html', {'form': form})

def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_list')
    return render(request, 'app/categoria_confirm_delete.html', {'categoria': categoria})


## Editora [feature/andre]

def editora_list(request):
    editoras = Editora.objects.all()
    return render(request, 'app/editora_list.html', {'editoras': editoras})

def editora_create(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('editora_list')
    else:
        form = EditoraForm()
    return render(request, 'app/editora_form.html', {'form': form})

def editora_update(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    if request.method == 'POST':
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            form.save()
            return redirect('editora_list')
    else:
        form = EditoraForm(instance=editora)
    return render(request, 'app/editora_form.html', {'form': form})

def editora_delete(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    if request.method == 'POST':
        editora.delete()
        return redirect('editora_list')
    return render(request, 'app/editora_confirm_delete.html', {'editora': editora})