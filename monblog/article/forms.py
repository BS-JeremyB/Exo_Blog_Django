from django import forms
from django.forms import ModelForm
from .models import Article
from django.contrib.auth.models import User

# class Create_article_form(forms.Form):
#     titre = forms.CharField(max_length=100)
#     # reste des autres propriétés

class Formulaire_creation_article(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        error_message = {
            'titre': {
                'max_length': "Ce titre dépasse la taille max"
            }
        }