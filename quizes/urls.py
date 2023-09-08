from django.urls import path
from .views import (
    quiz_list,
    quiz_view,
    )

app_name = "quizes"

urlpatterns = [
    path('', quiz_list, name='main-view'),
    path('<pk>/', quiz_view, name="quiz-view"),
]
