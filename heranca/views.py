from django.shortcuts import render
from allauth.account.forms import LoginForm, SignupForm
from django.contrib.auth.decorators import login_required
from .models import Noticia, Dict_indigenous, Dict_letter
from django.urls import reverse_lazy


def index(request):
    page_title = "Herança!"
    user = request.user 
    if user.is_authenticated:
        page_title = f"Herança - {user.username.title()}"
    login_form = LoginForm()
    signup_form = SignupForm() 
    noticias = Noticia.objects.filter(is_public=True)
    
    return render(request, 'heranca/herança.html', {'page_title': page_title,'noticias': noticias,'login_form': login_form,'signup_form': signup_form, 'user':user,})


@login_required(login_url=reverse_lazy('index'))
def profile(request):
    return reverse_lazy("index")


def dict_indigenous(request):
    page_title = "Herança - Dicionario"
    letters = Dict_letter.objects.order_by('alphabetical_order')
    
    return render(request, 'heranca/dict.html', {
        'page_title': page_title, 
        'letters':letters,
    })

