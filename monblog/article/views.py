from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Formulaire_creation_article

# Create your views here.


def article_list(request):
    return render(request, 'articles/article_list.html')

def article_create(request):
    if request.method == 'POST':
        form = Formulaire_creation_article(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('article_list')

    return render(request, 'articles/article_create.html', {'form': Formulaire_creation_article})
