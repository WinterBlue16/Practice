from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:4]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'lucky/index.html', context)

def detail(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'lucky/detail.html', {'question':q})

def results(request, question_id):
    response = "{}번 설문 결과입니다."
    return HttpResponse(response.format(question_id))

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice_select'])
    except:
        context = {'question':question, 'error_message':"You didn't select a choice."}
        return render(request, 'lucky/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('lucky:results', question_id = question.id)
        
