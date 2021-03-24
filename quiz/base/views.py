from django.shortcuts import render


# Create your views here.
from quiz.base.models import Question


def home(firstrequest):
    return render(firstrequest, 'base/home.html')


def classification(firstrequest):
    return render(firstrequest, 'base/classification.html')


def questions(firstrequest, index):
    question = Question.objects.filter(trueOrFalse=True).order_by('id')[index - 1]
    templateContext = {'indexOfQuestion': index, 'question': question}
    return render(firstrequest, 'base/game.html', context=templateContext)
