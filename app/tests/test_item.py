# app/tests/test_item.py
import pytest
from django.urls import reverse
from app.models import Item

@pytest.mark.django_db
class TestItemCRUD:
    @pytest.fixture(autouse=True)
    def init_items(self):
        Item.objects.create(name="Item1", description="Descrição 1")

    def test_item_listagem(self, client):
        url = reverse('item_list')
        response = client.get(url)
        assert response.status_code == 200
        assert b"Item1" in response.content

    def test_criar_item(self, client):
        url = reverse('item_create')
        response = client.post(url, {'name': 'NovoItem', 'description': 'Desc Novo'})
        assert response.status_code == 302
        assert Item.objects.filter(name="NovoItem").exists()

    def test_editar_item(self, client):
        item = Item.objects.first()
        url = reverse('item_update', args=[item.pk])
        response = client.post(url, {'name': 'ItemEditado', 'description': 'Desc Edit'})
        assert response.status_code == 302
        item.refresh_from_db()
        assert item.name == "ItemEditado"


    def test_deletar_item(self, client):
        item = Item.objects.first()
        url = reverse('item_delete', args=[item.pk])
        response = client.post(url)
        assert response.status_code == 302
        assert Item.objects.count() == 0

    def test_criar_item_invalido(self, client):
        url = reverse('item_create')
        # Enviar sem o campo 'name', que é obrigatório
        response = client.post(url, {'name': '', 'description': 'Sem nome'})
        # Esperamos que a view reexiba o formulário (status 200) e não crie o objeto
        assert response.status_code == 302
        assert b'This field is required' in response.content or b'Este campo é obrigatório' in response.content
        assert Item.objects.filter(description="Sem nome").count() == 0