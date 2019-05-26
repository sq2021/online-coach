from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
        form.instance.author = request.user
        form.instance.question_id = question.id
        if form.is_valid():
            form.save()
            return render(request, "qa/view.html", {'question': question})
    form = AnswerForm()
    return render(request, "qa/view.html", {'question': question, 'form': form})

class QuestionNewView(CreateView):
    model = Question
    fields = ['question_title', 'question_text', 'category']
    template_name = 'qa/new_question.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ['question_title', 'question_text', 'category']
    template_name = 'qa/new_question.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False
    