from django.contrib import admin
from .models import Quiz, QuizRelated

admin.site.register(QuizRelated)
admin.site.register(Quiz)
