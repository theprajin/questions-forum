from django.contrib import admin
from apps.forum.models import Question,UserQuestion, UserAnswer, VotedUp


admin.site.register(Question)
admin.site.register(UserQuestion)
admin.site.register(UserAnswer)
admin.site.register(VotedUp)

