from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.utils import timezone
from .models import Question, Answer
from .forms import AnswerForm, QuestionForm

def index(request):
    # Fetch 5 latest questions
    questions = Question.objects.all().order_by('-pub_date')[:10]
    context = {
        'latest_questions_list': questions
    }
    return render(request, 'qa/index.html', context)

def view(request, question_id):
    # Fetch question from database 
    question = get_object_or_404(Question, id = question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "qa/view.html", {'question': question})
    form = AnswerForm()
    return render(request, "qa/view.html", {'question': question, 'form': form})

def new(request):
    # create a new question
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return render(request, "qa/view.html")
    form = QuestionForm()
    return render(request, "qa/new_question.html", {'form': form})
    
    