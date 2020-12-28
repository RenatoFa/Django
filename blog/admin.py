from django.contrib import admin
from .models import Post

# Register your models here.
# Criar mais um componente no admin do django

# registra o modelo para aparecer a interface


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated")
    # preechimento do slug automatico (prepopulated_fields)
    prepopulated_fields = {"slug": ("title",)}
