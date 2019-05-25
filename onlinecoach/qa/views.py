from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.utils import timezone
from .models import Question, Answer

def index(request):
    # Fetch 5 latest questions
    questions = Question.objects.all().order_by('-pub_date')[:5]
    context = {
        'latest_questions_list': questions
    }
    return render(request, 'qa/index.html', context)

def view(request, question_id):
    # Fetch question from database 
    question = get_object_or_404(Question, id = question_id)
    return render(request, "qa/view.html", {'question': question})
    