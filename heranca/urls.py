from django.urls import path
from allauth.account.views import login, signup
from django.urls import reverse_lazy
from . import views

urlpatterns = [
    path('accounts/login/', login, name='account_login'),
    path('accounts/signup/', signup, name='account_signup'),
    path('', views.index, name='index'),
    path('2/', views.index2, name='index2'),
    path('accounts/profile/', views.profile, name='profile'),
    path('verify_login/', views.verify_login, name='verify_login'),
    
]
