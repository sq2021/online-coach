from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    question_title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    is_solved = models.BooleanField('is solved', default=False)
    category = models.IntegerField(default=1)
    
    def __str__(self):
        return self.question_text

    class Meta:
        ordering = ['-pub_date'] 

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    def __str__(self):
        return self.answer_text

    class Meta:
        ordering = ['-pub_date'] 
