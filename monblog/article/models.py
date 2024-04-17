from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.ForeignKey(User, on_delete=models.RESTRICT)
    contenu = models.TextField()

    def __str__(self):
        return f'{self.titre} par {self.auteur}'
