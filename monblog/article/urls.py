from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name="article_list"),
    path('article/create/', views.article_create)
]
