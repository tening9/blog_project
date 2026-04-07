from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)


urlpatterns = [
    path('', ArticleListView.as_view(), name='accueil'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='detail_article'),
    path('article/nouveau/', ArticleCreateView.as_view(), name='creer_article'),
    path('article/<int:pk>/modifier/', ArticleUpdateView.as_view(), name='modifier_article'),
    path('article/<int:pk>/supprimer/', ArticleDeleteView.as_view(), name='supprimer_article'),
]