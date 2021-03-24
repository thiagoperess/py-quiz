from django.contrib import admin

# Register your models here.
from quiz.base.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'enunciatedQuestion', 'trueOrFalse')
