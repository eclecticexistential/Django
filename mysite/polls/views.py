from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import bleach

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	
	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
		
class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'
	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now())
	
class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html',{'question':question,'error_message':"You didn't select a choice.",})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		#always do so no double post
		return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
	
def add(request):
	if request.method == 'POST':
		sentence = request.POST.get('question',None)
		question = bleach.clean(sentence)
		one = request.POST.get('one',None)
		two = request.POST.get('two',None)
		three = request.POST.get('three',None)
		four = request.POST.get('four',None)
		add_Quest = Question(question_text=question, pub_date=timezone.now())
		add_Quest.save()
		if one:
			add_Quest.choice_set.create(choice_text=one, votes=0)
		if two:
			add_Quest.choice_set.create(choice_text=two, votes=0)
		if three:
			add_Quest.choice_set.create(choice_text=three, votes=0)
		if four:
			add_Quest.choice_set.create(choice_text=four, votes=0)
		if add_Quest.choice_set.count() == 0:
			add_Quest.choice_set.create(choice_text="Yes", votes=0)
			add_Quest.choice_set.create(choice_text="Maybe", votes=0)
			add_Quest.choice_set.create(choice_text="No.", votes=0)
		return HttpResponseRedirect(reverse('polls:detail',args=(add_Quest.id,)))
	else:
		return render(request, 'polls/add.html')