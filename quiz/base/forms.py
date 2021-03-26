from django.forms import ModelForm

from quiz.base.models import userQuiz


class userQuizForm(ModelForm):
    class Meta:
        model = userQuiz
        fields = ['nome', 'email']
