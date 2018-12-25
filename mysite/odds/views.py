from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import get_stats
# Create your views here.

def index(request):
	current_standings = get_stats("Tokido","Momochi")
	context = {'matches':current_standings[0],'games':current_standings[1],'won':current_standings[2]}
	return render(request, 'odds/index.html',context)
	
def player_search(request):
	if request.method == 'POST':
		player_name = request.POST.get('player', None)
		opp_name = request.POST.get('opp', None)
		current_standings = get_stats(player_name, opp_name)
		context = {'matches':current_standings[0],'games':current_standings[1],'won':current_standings[2],'player':player_name, 'opp':opp_name}
		return render(request, 'odds/results.html', context)
	else:
		return render(request, 'odds/player_search.html')
	
def results(request):
	return render(request, 'odds/results.html')
