from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import URL

# Create your views here.
def index(request):
	url_list = URL.objects.all()
	context = { 'url_list' : url_list}
	return render(request, 'scrape/index.html', context)

def detail(request, url_id):
	try:
		url_link = URL.objects.get(pk = url_id)
	except URL.DoesNotExist:
		raise Http404("URL not scrapped.")
	return render(request, 'scrape/detail.html', {'url_link': url_link})
	
def add_urls(request):
	if request.method == 'POST':
		hyperlink = request.POST.get('textfield', None)
		new_url = URL(url=hyperlink, get_date=timezone.now())
		new_url.save()
		return HttpResponseRedirect('scrape/index.html')
	else:
		return render(request, 'scrape/add_urls.html')