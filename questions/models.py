from django.db import models
from quizes.models import Quiz
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    text = models.CharField(_("Text"), max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    text = models.CharField(_("Text"), max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'question: {self.question.text}, answer: {self.text}, correct: {self.correct}'
