# Vamos criar as nossas urls para Viewa
from django.urls import path

from . import views

app_name = "blog"  # variavel que vai referenciar nossa url

urlpatterns = [
    # conectando a url sem argumento com a view list
    path("", views.PostListView.as_view(), name="list"),
    # conectando a url com a slug do Post
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail")
]
