from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.test import TestCase
# from django.template import loader

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DeleteView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DeleteView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You Didnt Select A Choice",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class QuestionResultsViewTests(TestCase):
    '''Future Question and Past Question'''
    def test_future_question(self):
        future_question = create_question(question_text="Future question?", days=61)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.geturl(url)
        self.assertEqual(response.status_code,404)

    def test_past_question(self):
        past_question = create_question(question_text="Past question?", days=61)
        url = reverse('polls:results', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

class QuestionDetailViewTests(TestCase):
    '''Future Question and Past Question'''
    def test_future_question(self):
        future_question = create_question(question_text="Future question?", days=61)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.geturl(url)
        self.assertEqual(response.status_code,404)

    def test_past_question(self):
        past_question = create_question(question_text="Past question?", days=61)
        url = reverse('polls:results', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)



        # def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5] #Getting info from database
#     # template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     # return HttpResponse(f'Your Looking at Question {question_id}')
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question Does Not Exist")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#     # return HttpResponse(f'You Are Looking At The Results of Question {question_id}')