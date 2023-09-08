from django.db import models
from quizes.models import Quiz
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(_("Score"))
    
    def __str__ (self):
        return str(self.pk)
