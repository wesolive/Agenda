from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Evento(models.Model):#criando classe evento com os itens
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='data do evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)# variavel usuario armazena os usuarios do django

    class Meta: # alteração do nome da tabela
        db_table = 'evento'

    def __str__(self): # alterando cada evento recebe o nome do titulo
        return self.titulo

    def get_data_criacao(self):# alterando a exibição da data_evento
        return self.data_evento.strftime('%d/%m/%Y %H:%M hrs')