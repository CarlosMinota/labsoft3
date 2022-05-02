from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Question
from django.template import loader
from django.http import Http404


def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('controlProyecto/index.html')
    contex = {'lastest_question_list': lastest_question_list}
    #output = ''.join([q.question_text for q in lastest_question_list])
    #return HttpResponse(output)
    return render(request, 'controlProyecto/index.html', contex)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("La pregunta NO existe!")
    return render(request, 'controlProyecto/detail', {'question':question})

def results(request, question_id):
    response = "Esta es la pagina de resultados de la pregunta %s" %question_id
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("Estas votando en la pregunta %s" %question_id)