from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import URL

# Create your views here.
def index(request):
	url_list = URL.objects.all()
	context = { 'url_list' : url_list}
	return render(request, 'scrape/index.html', context)

def detail(request, url_id):
	url_link = get_object_or_404(URL, pk=url_id)
	return render(request, 'scrape/detail.html', {'url_link': url_link})
	
def add_urls(request):
	if request.method == 'POST':
		hyperlink = request.POST.get('textfield', None)
		tag_name = request.POST.get('tagName', None)
		new_url = URL(url=hyperlink, tag=tag_name, get_date=timezone.now())
		new_url.save()
		return HttpResponseRedirect('/scrape/{0}'.format(new_url.id))
	else:
		return render(request, 'scrape/add_urls.html')