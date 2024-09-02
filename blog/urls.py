from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_article, name='list_article'),
    path('article/<int:article_id>/', views.detail_article, name='detail_article'),
    path('article/creer/', views.creer_article, name='creer_article'),
    path('article/<int:article_id>/modifier/', views.modifier_article, name='modifier_article'),
    path('article/<int:article_id>/supprimer/', views.supprimer_article, name='supprimer_article'),
]
