# app/tests/test_item.py
import pytest
from django.urls import reverse
from app.models import Editora

@pytest.mark.django_db
class TestItemCRUD:
    @pytest.fixture(autouse=True)
    def init_editora(self):
        Editora.objects.create(name="Editora1")

    def test_editora_listagem(self, client):
        url = reverse('editora_list')
        response = client.get(url)
        assert response.status_code == 200
        assert b"Editora1" in response.content

    def test_criar_editora(self, client):
        url = reverse('editora_create')
        response = client.post(url, {'name': 'NovoEditora'})
        assert response.status_code == 302
        assert Editora.objects.filter(name="NovoEditora").exists()

    def test_editar_editora(self, client):
        editora = Editora.objects.first()
        url = reverse('editora_update', args=[editora.pk])
        response = client.post(url, {'name': 'EditoraEditado'})
        assert response.status_code == 302
        editora.refresh_from_db()
        assert editora.name == "EditoraEditado"


    def test_deletar_editora(self, client):
        editora = Editora.objects.first()
        url = reverse('editora_delete', args=[editora.pk])
        response = client.post(url)
        assert response.status_code == 302
        assert Editora.objects.count() == 0
