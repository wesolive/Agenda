from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
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
    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento > datetime.now():
            return True
        else:
            return False