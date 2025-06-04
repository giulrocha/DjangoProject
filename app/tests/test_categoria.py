# app/tests/test_item.py
import pytest
from django.urls import reverse
from app.models import Categoria

@pytest.mark.django_db
class TestItemCRUD:
    @pytest.fixture(autouse=True)
    def init_categoria(self):
        Categoria.objects.create(name="Categoria1")

    def test_categoria_listagem(self, client):
        url = reverse('categoria_list')
        response = client.get(url)
        assert response.status_code == 200
        assert b"Categoria1" in response.content

    def test_criar_categoria(self, client):
        url = reverse('categoria_create')
        response = client.post(url, {'name': 'NovoCategoria'})
        assert response.status_code == 302
        assert Categoria.objects.filter(name="NovoCategoria").exists()

    def test_editar_categoria(self, client):
        categoria = Categoria.objects.first()
        url = reverse('categoria_update', args=[categoria.pk])
        response = client.post(url, {'name': 'CategoriaEditado'})
        assert response.status_code == 302
        categoria.refresh_from_db()
        assert categoria.name == "CategoriaEditado"


    def test_deletar_categoria(self, client):
        categoria = Categoria.objects.first()
        url = reverse('categoria_delete', args=[categoria.pk])
        response = client.post(url)
        assert response.status_code == 302
        assert Categoria.objects.count() == 0
