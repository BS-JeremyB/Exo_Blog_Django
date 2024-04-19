from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name="article_list"),
    path('article/<int:id>', views.article_detail, name='article_detail'),
    path('article/create/', views.article_create, name='article_create'),
    path('article/delete/<int:id>', views.article_delete, name='article_delete'),
    path('article/update/<int:id>', views.article_update, name='article_update')
]
