from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question = models.CharField(max_length=250)
    

class UserQuestion(models.Model):
    questioned_by = models.ForeignKey(User, related_name='questioned_by', on_delete= models.CASCADE)
    question = models.OneToOneField(Question, related_name='questions', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.question


class UserAnswer(models.Model):
    answered_by = models.ForeignKey(User, related_name='answered_by', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now=True)
    answer = models.TextField()

    def __str__(self):
        return self.answer


class VotedUp(models.Model):
    voted_by = models.ForeignKey(User, related_name='voted_by', on_delete=models.DO_NOTHING)
    to_answer = models.ForeignKey(UserAnswer, related_name='to_answer', on_delete=models.DO_NOTHING)
    voted_on = models.DateTimeField(auto_now_add = True)
    voted_down = models.BooleanField()
