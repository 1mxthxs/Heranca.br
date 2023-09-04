from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from questions.models import Question, Answer
from results.models import Result
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required

class QuizListView(ListView):
    model = Quiz
    template_name = 'quizes/main.html'

@login_required(login_url=reverse_lazy('account_login'))
def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
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
            'page_title':"GET",
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
                
                
        score_ = score * multiplier
        response = []
        passed = True
        Result.objects.create(quiz=quiz, user=user, score=score_)
        if score_ >= quiz.required_score_to_pass: 
            passed = True
        else:
            passed = False
            
        response.append({
                'passed': passed,
                'score': score_,
                'results': results,
            })

        return render(request, 'quizes/quiz.html', {
            'obj': quiz,
            'data': questions,
            'result': True,
            'page_title':response,
            'response': response,
            'passed': passed,
            'score': score_,
            'results': results,

        })