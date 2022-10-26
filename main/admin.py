from django.contrib import admin
from main.models import Cliente, Locacao, Filme, Categoria

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Locacao)
admin.site.register(Filme)
admin.site.register(Categoria)