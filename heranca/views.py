from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .models import Post, New, Dict_indigenou, Dict_letter
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def index(request):
    page_title = "Inicio!"
    user = request.user 
    if user.is_authenticated:
        page_title = user.username.title()
    news = New.objects.filter(is_public=True)
    
    return render(request, 'heranca/pages/herança.html', {'page_title': page_title, 'news': news, 'user': user,})


@login_required(login_url=reverse_lazy('index'))
def profile(request):
    return redirect(reverse("index"))


@csrf_protect
def dict_indigenous(request):
    page_title = "Dicionario"
    search_placeholder_text = "Busque pela letra!"
    letters = Dict_letter.objects.order_by('alphabetical_order')
    
    if request.method == "GET":
        page_title = "GET"
    elif request.method == 'POST':
        search_text = str(request.POST.get('header-search', '')).title()
        print(f'Search: {search_text}')
        search_result = letters.filter(
            Q(letter_char__icontains=search_text))
        letters = search_result
    
    return render(request, 'heranca/pages/dict.html', {
        'page_title': page_title,
        'letter_detail': False,
        'letters': letters,
        'search_placeholder_text': search_placeholder_text,
        'text_value': '',
    })
    

def dict_details(request, char):
    letter = get_object_or_404(
        Dict_letter,
        letter_char=char,
    )
    more_dict = Dict_letter.objects.exclude(letter_char=char).order_by("?")[:3]    
    
    page_title = f"Dicionario - {letter.letter_char}"
    
    return render(request, 'heranca/pages/dict.html', {
        'page_title': page_title,
        'letter_detail': True,
        'letter': letter,
        'more_dict': more_dict,
    })

def about(request):
    return render(request, 'heranca/pages/about.html',{
        'page_title': "Quem somos",
    })


def after_login(request):
    return render(request, 'heranca/pages/after_login.html',{
        'page_title':"After Login",
        
    })
    
def community(request):
    user = request.user
    posts = Post.objects.filter(is_public=True)

    liked_posts = {}
    for post in posts:
        liked_posts[post.id] = user.is_authenticated and post.likes.filter(id=user.id).exists()

    return render(request, 'heranca/pages/community.html', {
        'page_title': "Community",
        'posts': posts,
        'liked_posts': liked_posts,
        'liked':post.liked(request.user),
    })



from django.shortcuts import redirect

def like_post(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        post.like(request.user)
    return redirect('community') 
