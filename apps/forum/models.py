from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()

class Question(models.Model):
    question = models.CharField(max_length=250)

    def __str__(self):
        return self.question
    

class UserQuestion(models.Model):
    questioned_by = models.ForeignKey(User, related_name='forum_questions', on_delete= models.CASCADE)
    question = models.ForeignKey(settings.QUESTION_MODEL, related_name='questions', on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'question descriptions'
        unique_together = ('question',)

    def __str__(self):
        return self.description


class UserAnswer(models.Model):
    answered_by = models.ForeignKey(User, related_name='forum_answers', on_delete=models.CASCADE)
    answered_to = models.ForeignKey(settings.QUESTION_MODEL, related_name='answers', on_delete=models.CASCADE)
    answer = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'answers'

    def __str__(self):
        return self.answer


class VotedUp(models.Model):
    voted_by = models.ForeignKey(User, related_name='votes', on_delete=models.CASCADE)
    to_answer = models.ForeignKey(UserAnswer, related_name='to_answer', on_delete=models.CASCADE)
    voted_down = models.BooleanField()
    voted_on = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'votes'