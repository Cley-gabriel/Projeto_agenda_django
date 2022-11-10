from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email 
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    return render (request, 'accounts/login.html')

def logout(request):
    return render (request, 'accounts/logout.html')

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

    #validação de senha
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

    

def dashboard(request):
    return render (request, 'accounts/dashboard.html')
