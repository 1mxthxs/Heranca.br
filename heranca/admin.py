from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import Noticia

@admin.register(Noticia)
class NoticiaAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass
