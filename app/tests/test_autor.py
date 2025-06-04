# app/tests/test_item.py
import pytest
from django.urls import reverse
from app.models import Autor

@pytest.mark.django_db
class TestItemCRUD:
    @pytest.fixture(autouse=True)
    def init_autor(self):
        Autor.objects.create(name="Autor1")

    def test_autor_listagem(self, client):
        url = reverse('autor_list')
        response = client.get(url)
        assert response.status_code == 200
        assert b"Autor1" in response.content

    def test_criar_autor(self, client):
        url = reverse('autor_create')
        response = client.post(url, {'name': 'NovoAutor'})
        assert response.status_code == 302
        assert Autor.objects.filter(name="NovoAutor").exists()

    def test_editar_autor(self, client):
        autor = Autor.objects.first()
        url = reverse('autor_update', args=[autor.pk])
        response = client.post(url, {'name': 'AutorEditado'})
        assert response.status_code == 302
        autor.refresh_from_db()
        assert autor.name == "AutorEditado"


    def test_deletar_autor(self, client):
        autor = Autor.objects.first()
        url = reverse('autor_delete', args=[autor.pk])
        response = client.post(url)
        assert response.status_code == 302
        assert Autor.objects.count() == 0
