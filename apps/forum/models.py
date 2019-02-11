from django.db import models
from django.contrib.auth.models import User


class UserQuestion(models.Model):
    questioned_by = models.ForeignKey(User, related_name='questions', on_delete= models.CASCADE, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    question = models.TextField()

    def __str__(self):
        return self.question


class UserAnswer(models.Model):
    answered_by = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE, null=False)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now=True)
    answer = models.TextField()

    def __str__(self):
        return self.answer


class VotedUp(models.Model):
    voted_by = models.ForeignKey(User, related_name='votes', on_delete=models.DO_NOTHING)
    to_answer = models.ForeignKey(UserAnswer, related_name='to_answers', on_delete=models.DO_NOTHING)
    voted_on = models.DateTimeField(auto_now_add = True)
    voted_down = models.BooleanField(default=False, null=False)
