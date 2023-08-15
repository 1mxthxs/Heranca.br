from django.shortcuts import render

def index(request):
    return render(request, 'heranca/herança.html')

def index2(request):
    return render(request, 'heranca/psychic-goggles-main/herança.html')
