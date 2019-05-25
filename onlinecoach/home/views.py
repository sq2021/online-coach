from django.shortcuts import render
from django.utils import timezone
from qa.views import Question

# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        'latest_questions_list': questions
    }
    return render(request, 'home/index.html', context)