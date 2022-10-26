from django.db import models

# Create your models here.

class Locacao(models.Model):
    data_entrega = models.DateField()
    data_locacao = models.DateField()
    valor = models.DecimalField(decimal_places=2,max_digits=10)
    
    def __str__(self):
        return self.valor

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    cliente = models.ForeignKey(Locacao,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    ano_lancamento = models.IntegerField()
    valor_locacao = models.DecimalField(decimal_places=2,max_digits=10)
    locacao = models.ManyToManyField(Categoria)
    categoria = models.ForeignKey(Locacao,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo