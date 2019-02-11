from django.contrib import admin
from apps.forum.models import Question,UserQuestion, UserAnswer, VotedUp


admin.site.register(Question)


@admin.register(UserQuestion)
class UserQuestionAdmin(admin.ModelAdmin):
    list_display = ('description','question' ,'questioned_by', 'created_date', 'updated_date')
    list_filter = ( 'created_date',)


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'answered_to', 'answered_by', 'created_date', 'updated_date')
    list_filter = ('answered_to',)


@admin.register(VotedUp)
class VotedUpAdmin(admin.ModelAdmin):
    list_display = ('voted_by', 'to_answer', 'voted_down', 'voted_on')

