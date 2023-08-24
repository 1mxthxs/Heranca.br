from django.shortcuts import render, redirect
from allauth.account.forms import LoginForm, SignupForm
from django.contrib.auth.decorators import login_required
from .models import Noticia, Dict_indigenous, Dict_letter
from django.urls import reverse_lazy,reverse


def index(request):
    page_title = "Herança!"
    user = request.user 
    if user.is_authenticated:
        page_title = f"Herança - {user.username.title()}"
    login_form = LoginForm()
    signup_form = SignupForm() 
    noticias = Noticia.objects.all()
    
    return render(request, 'heranca/herança.html', {'page_title': page_title,'noticias': noticias,'login_form': login_form,'signup_form': signup_form, 'user':user,})


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

    return reverse("index")


def dict_indigenous(request):
    page_name = "Herança - Dicionario"
    dict_obj = Dict_indigenous.objects.all()
    letter_dict = Dict_indigenous.objects.all()
    
    return render(request, 'heranca/dict.html', name="dict")

