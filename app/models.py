from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    #editora = models.ForeignKey('Editora', on_delete=models.CASCADE)



    def __str__(self):
        return self.name


class Categoria(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Autor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

