from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/profile/', views.profile, name='profile'),
    path('profile/', views.profile_logged, name='profile_logged'),
    path('dict/', views.dict_indigenous, name='dict_indigenous'),
    path('dict/<str:char>', views.dict_details, name='dict_details'),
    path('about/', views.about, name='about'),
    path('after_login/', views.after_login, name="after_login"),
    path('community/', views.community, name="community"),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),


]
