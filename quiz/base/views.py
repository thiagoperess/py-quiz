from django.shortcuts import render, redirect

# Create your views here.
from quiz.base.forms import userQuizForm
from quiz.base.models import Question, userQuiz


def home(firstrequest):
    if firstrequest.method == 'POST':
        # user already exists
        email = firstrequest.POST['email']
        try:
            user = userQuiz.objects.get(email=email)
        except userQuiz.DoesNotExist:
            # user not exists
            formulario = userQuizForm(firstrequest.POST)
            if formulario.is_valid():
                user = formulario.save()
                firstrequest.session['user_id'] = user.id
                return redirect('/questions/1')
            else:
                contexto = {'formulario': formulario}
                return render(firstrequest, 'base/home.html', contexto)
        else:
            firstrequest.session['user_id'] = user.id
            return redirect('/questions/1')


    return render(firstrequest, 'base/home.html')


def classification(firstrequest):
    return render(firstrequest, 'base/classification.html')


def questions(firstrequest, index):
    try:
        user_id = firstrequest.session['user_id']
    except KeyError:
        return redirect('/')
    else:
        question = Question.objects.filter(trueOrFalse=True).order_by('id')[index - 1]
        templateContext = {'indexOfQuestion': index, 'question': question}
        return render(firstrequest, 'base/game.html', context=templateContext)
