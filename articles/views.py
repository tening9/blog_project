
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'articles/liste.html'
    context_object_name = 'articles'
    ordering = ['-date_publication']

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/detail.html'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'articles/form.html'
    fields = ['titre', 'contenu', 'image']  

    def form_valid(self, form):
        form.instance.auteur = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'articles/form.html'
    fields = ['titre', 'contenu', 'image']

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'articles/supprimer.html'
    success_url = reverse_lazy('accueil')