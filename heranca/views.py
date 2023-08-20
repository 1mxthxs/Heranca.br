from django.shortcuts import render, redirect
from allauth.account.forms import LoginForm, SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Noticia
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect


def index(request):
    error_message = request.GET.get('error', None)
    user = request.user 
    login_form = LoginForm()  # Instância do formulário de login
    signup_form = SignupForm() 
    page_title = "Herança!"
        
    noticias = Noticia.objects.all()
    
    return render(request, 'heranca/herança.html', {'page_title': page_title,'noticias': noticias,'login_form': login_form,'signup_form': signup_form, 'error_message': error_message,})

def index2(request):
    return render(request, 'heranca/psychic-goggles-main/herança.html')


@require_POST
@csrf_protect
def verify_login(request):
    username = request.POST.get('login')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse("index"))
    else:
        error_message = "Usuário ou senha incorretos."
        return redirect(reverse('index') + f'?error={error_message}')


@login_required(login_url=reverse_lazy('index'))
def profile(request):
    noticias = Noticia.objects.all()
    user = request.user
    if user.first_name:
        page_title = f'Perfil - {user.first_name.title()}'
    else:
         page_title = f'Perfil - {user.username.title()}'
    login_form = LoginForm()
    signup_form = SignupForm()

    context = {'request': request,'page_title': page_title, 'user':user,'noticias': noticias,'login_form': login_form,
        'signup_form': signup_form,}

    return render(request, 'heranca/herança.html', context=context)
