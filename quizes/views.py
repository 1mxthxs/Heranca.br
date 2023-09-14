from django.shortcuts import render
from .models import Quiz, QuizRelated
from django.views.generic import ListView
from django.http import JsonResponse
from questions.models import Question, Answer
from results.models import Result
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required


@login_required(login_url=reverse_lazy('account_login'))
def quiz_list(request):
    quizes = Quiz.objects.filter(is_public=True)
    quiz_related = QuizRelated.objects.all()
    quiz_data = []

    for quiz in quizes:
        if request.user.is_authenticated:
            user_result = quiz.get_user_result(request.user)
        else:
            user_result = "N/A"
        quiz_data.append({
            'quiz': quiz,
            'user_result': user_result,
            'quiz_related': quiz_related,
        }) 
   
    return render(request, 'quizes/main.html', {
        'quiz_data': list(quiz_data),
        'quiz_related': quiz_related,
        'user_result': user_result,
        'page_title': 'Quiz',
        'quiz': None,
    })
        

@login_required(login_url=reverse_lazy('account_login'))
def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    page_title = quiz.name
    if request.method == "GET":
        questions = []
        number = 0
        for quest in quiz.get_questions():
            answers = []
            for ans in quest.get_answers():
                answers.append(ans.text)
            questions.append({str(quest): answers})
            number +=1    
        return render(request, 'quizes/quiz.html', {
            'obj': quiz,
            'data': questions,
            'result': False,
            'page_title': page_title,
            'quiz': True,
            'background_quiz': True,
        })
    elif request.method == "POST":
        data = request.POST
        questions = []
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
    
        for k in data_.keys():
            question = Question.objects.get(text=k)
            questions.append(question)
        user = request.user
        quiz = Quiz.objects.get(pk=pk)
        
        score = 0
        multiplier = 100 / quiz.number_of_questions
        class Res:
            def __init__(self, question, correct_answer, answered):
                self.question = question
                self.correct_answer = correct_answer
                self.answered = answered
        
        results = []        
        for q in questions:
            a_selected = request.POST.get(q.text)       
            correct_answer = None
            if a_selected is not None:
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text
                          
                            
                result = Res(str(q), correct_answer, a_selected)
                results.append(result)
                print(f'Select: {a_selected}')
            if a_selected is None:
                result = Res(str(q), correct_answer, 'Not answered!')
                results.append(result)
                
        response = []
        passed = True
        Result.objects.create(quiz=quiz, user=user, score=score)
        if score < quiz.required_score_to_pass: 
            passed = False
        else:
            passed = True
            
        response.append({
                'passed': passed,
                'score': score,
                'results': results,
            })

        return render(request, 'quizes/quiz.html', {
            'obj': quiz,
            'data': questions,
            'result': True,
            'page_title': f'Repostas {page_title}',
            'response': response,
            'passed': passed,
            'score': score,
            'results': results,
            'quiz': True,
            'background_quiz': True,
        })