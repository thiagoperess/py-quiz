from django.contrib import admin

# Register your models here.
from quiz.base.models import Question, userQuiz


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'enunciatedQuestion', 'trueOrFalse')

@admin.register(userQuiz)
class userQuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'inscription')
