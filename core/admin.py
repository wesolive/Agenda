from django.contrib import admin
from core.models import Evento


# Register your models here.

class EventoAdmin(admin.ModelAdmin):# criação de uma classe com filtro e display list
    list_display = ('titulo', 'data_evento','data_criacao')
    list_filter = ('titulo','usuario','data_evento',)
admin.site.register(Evento,EventoAdmin)#registrando o models