from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco

class PontosTuristicos(models.Model):
    nome = models.CharField(max_length = 150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacao = models.ManyToManyField(Avaliacao)
    endereco = models.ManyToManyField(Endereco)
    foto = models.ImageField(upload_to='pontos_tur', null=True,blank=False)

    def __str__(self):
        return self.nome
