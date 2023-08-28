from django.shortcuts import render, get_object_or_404, redirect
from allauth.account.forms import LoginForm, SignupForm
from django.contrib.auth.decorators import login_required
from .models import Noticia, Dict_indigenous, Dict_letter
from django.urls import reverse_lazy, reverse


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
    return redirect(reverse("index"))


def dict_indigenous(request):
    page_title = "Herança - Dicionario"
    letters = Dict_letter.objects.order_by('alphabetical_order')
    
    return render(request, 'heranca/dict.html', {
        'page_title': page_title, 
        'letter_detail': False,
        'letters':letters,
    })
    

def dict_details(request, char):
    letter = get_object_or_404(
        Dict_letter,
        letter_char=char,
    )
    more_dict = Dict_letter.objects.exclude(letter_char=char).order_by("?")[:3]    
    
    page_title = f"Dicionario - {letter.letter_char}"
    
    return render(request, 'heranca/dict.html', {
        'page_title': page_title, 
        'letter_detail': True,
        'letter':letter,
        'more_dict': more_dict,
    })
    
    
def quiz(request):
    page_title = "Herança - Quiz"
    
    return render(request, 'heranca/quiz.html',{
        'page_title':page_title,
        
    })

