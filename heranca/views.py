from django.shortcuts import render
from .models import Noticia

def index(request):
    noticias = Noticia.objects.all()
    return render(request, 'heranca/herança.html', {'noticias': noticias,})

def index2(request):
    return render(request, 'heranca/psychic-goggles-main/herança.html')
