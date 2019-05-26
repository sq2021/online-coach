from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # reputation_points = models.IntegerField(default=0)
    # total_questions = models.IntegerField(default=0)
    # total_answers = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.email
    pass
