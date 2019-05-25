from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=500)
    question_title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    is_solved = models.BooleanField('is solved', default=False)
    category = models.IntegerField(default=1)
    
    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.answer_text
