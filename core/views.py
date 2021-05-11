from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#trabalhando com autenticação
def login_user(request):#caso não logado redireciona para login
    return render(request, 'login.html')
#criação da função logout
def logout_user(request):
    logout(request) #executa a função logout e limpaa sessão
    return redirect('/') #redireciona para a raiz

def submit_login(request):#submete os dados para validação
    if request.POST:#recebe usuario e senha e faz validação
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:#verifica se usuario esta em branco
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuario ou senha invalido!")
    return redirect('/')
@login_required(login_url='/login')#força o usuario estar logado para acessar
#fim autenticação


# criando lista de eventos a ser exibida
def lista_eventos(request):
    usuario = request.user #capitura o usuario da tabela django
    evento = Evento.objects.filter(usuario = usuario) # filtra o evento por usuario
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
