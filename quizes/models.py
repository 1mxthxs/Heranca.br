from django.db import models
from django.db.models import Case, When, Value
import random
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

DIFF_CHOICES = (
    (_('easy'), _('easy')),
    (_('medium'), _('medium')),
    (_('hard'), _('hard')),
)

class QuizRelated(models.Model):
    name = models.CharField(_("Name"),max_length=120)
    
    
    def __str__(self):
        return self.name
    
    def get_not_none(self):
        return self.quiz_set.all().filter(is_public=True).count()
    
    def get_quizes(self):
        return list(self.quiz_set.all().filter(is_public=True))
    

class Quiz(models.Model):
    name = models.CharField(_('Name'), max_length=120)
    topic = models.CharField(_('Topic'), max_length=120)
    number_of_questions = models.IntegerField(_("Number of Questions"))
    time = models.IntegerField(_("Time"),help_text=_("Time in Minutes"))
    required_score_to_pass = models.IntegerField(_("Required score to pass"), help_text=_('Required score, ex: 6, then (6=score/10=questions) to pass') )
    difficulty = models.CharField(_('Difficulty'), max_length=7, choices=DIFF_CHOICES, blank=True)
    quiz_related = models.ForeignKey(QuizRelated, on_delete=models.CASCADE)
    is_public = models.BooleanField(_('Is public'), default = True)
    
    def clean(self):
        if self.required_score_to_pass > self.number_of_questions or self.required_score_to_pass <= 0:
            raise ValidationError(_("required_score_to_pass should be less than or equal to the number_of_questions and greater than 0.\nRequired_score_to_pass < Number_of_questions"))
    
    
    def __str__(self):
        return f"{self.name} - {self.topic}"
    
    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]
    
    def get_user_result(self, user):
        if self.result_set.filter(user=user).exists():
            result = self.result_set.filter(user=user).last()
            score = result.score
        else:
            score = None
        return score
    
    
    class Meta:
        ordering = [
            Case(
                When(difficulty="easy", then=Value(1)),
                When(difficulty="medium", then=Value(2)),
                When(difficulty="hard", then=Value(3)),
                default=Value(4),
                output_field=models.IntegerField(),
            )
        ]
        verbose_name_plural = 'Quizes'
    
