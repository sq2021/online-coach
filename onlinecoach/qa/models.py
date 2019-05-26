from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from datetime import datetime

SPORT_CHOICES = [
    ('fo', 'Footbal'),
    ('ba', 'Basketball'),
    ('ic', 'Ice Hockey'),
    ('bs', 'Baseball'),
    ('ma', 'Martial Arts'),
    ('go', 'Golf'),
    ('te', 'Tennis'),
    ('sw', 'Swimming'),
    ('tr', 'Track'),
    ('vo', 'Volleyball'),
    ('gy', 'Gymnastics'),
    ('bo', 'Body Building'),
]
# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = HTMLField()
    question_title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published', default=datetime.now)
    is_solved = models.BooleanField('is solved', default=False)
    category = models.CharField(max_length=2, choices=SPORT_CHOICES)
    
    def __str__(self):
        return self.question_text

    class Meta:
        ordering = ['-pub_date'] 

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = HTMLField()
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    def __str__(self):
        return self.answer_text

    class Meta:
        ordering = ['-pub_date'] 
