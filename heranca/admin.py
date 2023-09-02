from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import New, Dict_indigenou, Dict_letter

@admin.register(New)
class NoticiaAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(Dict_indigenou)

class DictLetterAdmin(admin.ModelAdmin):
    list_display = ('letter_char', 'alphabetical_order')
    list_editable = ('alphabetical_order',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Atualize as posições alfabéticas com base no valor editado
        letters = Dict_letter.objects.all().order_by('alphabetical_order')
        for index, letter in enumerate(letters, start=1):
            letter.alphabetical_order = index
            letter.save()

admin.site.register(Dict_letter, DictLetterAdmin)
