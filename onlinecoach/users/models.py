from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete="models.CASCADE")
    reputation_count = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    total_answers = models.IntegerField(default=0)