from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Produto(models.Model):
              nome = models.CharField(max_length=100)
              quantidade = models.IntegerField()
              preco = models.DecimalField(max_digits=10, decimal_places=2)
              imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
              usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='produtos')

