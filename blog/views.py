# Criar as nossas views para o django
# Essas views podem ser criadas por function e classes

from django.views.generic import DetailView, ListView
from .models import Post
# ListView = Listar nossos post
# DetailView = Detalha o post


class PostListView(ListView):  # subclasse da  ListView
    model = Post


class PostDetailView(DetailView):  # subclasses da DetailView
    model = Post
