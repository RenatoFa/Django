from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# models do nosso app
# fonte unica e definitiva dos nossos dados
# cada model é uma classe python


# Class Post do blog ( Todo blog tem Post não confundir com o Post do padrao
# rest)
class Post (models.Model):
    # Todo blog tem um titulo (CharField é uma subclasse de models)
    title = models.CharField(max_length=255)
    # slug é o texto que vai ser usado na url
    slug = models.SlugField(max_length=255, unique=True)
    # exemplo  www.meusite/blog/introducao-ao-django
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Cada usuario tem um id unico
    body = models.TextField()
    # Corpo do post (Sem se preocupar com o tamanho do corpo)
    created = models.DateTimeField(auto_now_add=True)
    # Ao criar um post , vai adicionar automagicamente a hora e a data
    updated = models.DateTimeField(auto_now=True)
    # A diferença do auto_now_add é que ele vai atualizar a data e hora
    # (automatico)

    # Mudar o nome no admin do Post(object post para post)
    def __str__(self):
        return self.title

    # Essa parte vai criar uma tabela no nosso banco

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
    # Metodo para definir a url de um recurso(Metodo Post)

    class Meta:
        ordering = ("-created",)
