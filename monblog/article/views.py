from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import *
from .models import Article
from django.db.models import Q

# Create your views here.


def article_list(request):
    query = request.GET.get('query_filter', '')
    if query:
        articles = Article.objects.filter(
            Q(titre__icontains=query) |
            Q(auteur__username__icontains=query)
        )
    else:
        articles = Article.objects.all().order_by('id')
        
    return render(request, 'articles/article_list.html', {'articles_in_template' : articles})


def article_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'articles/article_detail.html', {'article_in_template': article})


def article_create(request):
    if not request.user.is_authenticated:
        return redirect('signin')


    if request.method == 'POST':
        form = Formulaire_creation_article(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('article_list')

    return render(request, 'articles/article_create.html', {'form': Formulaire_creation_article})


def article_delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('article_list')



def article_update(request, id):
    article = Article.objects.get(id=id)

    if request.method == 'POST':
        form = Formulaire_changer_article(request.POST, instance=article)
        if form.is_valid():
            form.save()
        return redirect('article_list')
    
    form = Formulaire_changer_article(instance=article)
    return render(request, 'articles/article_update.html', {'form_in_template': form})
        
    