from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#Criação das views
def login(request):
    if request.method != 'POST':
        return render (request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    
    #checando se o usuario vai autenticar.
    user = auth.authenticate(request, username=usuario, password=senha)

    #usuario null
    if not user:
        messages.error(request, 'Usuário ou senha inválida')
        return render (request, 'accounts/login.html')
    #usuario logado
    else:
        auth.login(request, user)
        messages.success(request, 'Login efetuado com sucesso.')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('dashboard')

def register(request):
    if request.method != 'POST':
        return render (request, 'accounts/register.html')
    
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode ficar vazio.')
        return render (request, 'accounts/register.html')

    #validação de email.
    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido.')
        return render (request, 'accounts/register.html')

    #validação de senha.
    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter mais de 5 caracteres.')
        return render (request, 'accounts/register.html')

    elif senha != senha2:
        messages.error(request, 'As senhas são diferentes.')
        return render (request, 'accounts/register.html')

    #Validação de usuário
    if len(usuario) < 3:
        messages.error(request, 'Usuário precisa ter mais de 3 caracteres.')
        return render (request, 'accounts/register.html')

    #verifica se o usuario já existe
    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe')
        return render (request, 'accounts/register.html')

    #verifica se o email já existe
    if User.objects.filter(email=email).exists():
        messages.error(request, 'E-mail já existe')
        return render (request, 'accounts/register.html')
    
    messages.success(request, 'Registrado com sucesso! Agora faça login.')
    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name = nome, last_name = sobrenome)
    user.save()
    return redirect('login')

    
@login_required(redirect_field_name='login')
def dashboard(request):
    return render (request, 'accounts/dashboard.html')
