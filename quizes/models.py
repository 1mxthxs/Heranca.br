from django.db import models
from django.db.models import Case, When, Value
import random
from django.core.exceptions import ValidationError

DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

class QuizRelated(models.Model):
    name = models.CharField(max_length=120)
    
    
    def __str__(self):
        return self.name
    
    def get_not_none(self):
        return self.quiz_set.all().filter(is_public=True).count()
    
    def get_quizes(self):
        return list(self.quiz_set.all().filter(is_public=True))
    

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Time in Minutes")
    required_score_to_pass = models.IntegerField(help_text='required score, ex: 6, then (6=score/10=questions) to pass', )
    difficulty = models.CharField(max_length=7, choices=DIFF_CHOICES, blank=True)
    quiz_related = models.ForeignKey(QuizRelated, on_delete=models.CASCADE)
    is_public = models.BooleanField(default = True)
    
    def clean(self):
        if self.required_score_to_pass > self.number_of_questions or self.required_score_to_pass <= 0:
            raise ValidationError("required_score_to_pass should be less than or equal to the number_of_questions and greater than 0.\nRequired_score_to_pass < Number_of_questions")
    
    
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
    
