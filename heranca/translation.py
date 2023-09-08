from . import models
from modeltranslation.translator import TranslationOptions, register


@register(models.New)
class NewTranslationOptions(TranslationOptions):
    fields = ('titulo', 'conteudo')