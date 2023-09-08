from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import New, Dict_indigenou, Dict_letter
from django.conf import settings 
from django.utils.translation import activate 
from modeltranslation.admin import TranslationAdmin
from modeltranslation.utils import get_language
from modeltranslation.translator import translator

class NewAdmin(TranslationAdmin):
    actions = ['duplicate_selected']

    def duplicate_selected(self, request, queryset):
        for obj in queryset:
            new_obj = New()
            for lang_code, _ in settings.LANGUAGES:
                activate(lang_code)
                for field_name in translator.get_options_for_model(New).get_field_names():
                    setattr(new_obj, f"{field_name}", getattr(obj, f"{field_name}"))
            
            # Copie outros campos não traduzidos
            new_obj.image = obj.image
            new_obj.is_public = obj.is_public
            new_obj.save()
        
        self.message_user(request, f"{queryset.count()} objetos New foram duplicados com sucesso.")

    duplicate_selected.short_description = "Duplicar objetos New selecionados"

admin.site.register(New, NewAdmin)


admin.site.register(Dict_indigenou)

class DictLetterAdmin(admin.ModelAdmin):
   
    list_display = ('letter_char', 'alphabetical_order')
    list_editable = ('alphabetical_order',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        letters = Dict_letter.objects.all().order_by('alphabetical_order')
        for index, letter in enumerate(letters, start=1):
            letter.alphabetical_order = index
            letter.save()
    

admin.site.register(Dict_letter, DictLetterAdmin)
