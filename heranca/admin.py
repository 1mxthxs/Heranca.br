from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import Noticia, Dict_indigenous, Dict_letter

@admin.register(Noticia)
class NoticiaAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(Dict_indigenous)
admin.site.register(Dict_letter)
