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
		sub_tag_name = request.POST.get('subName', None)
		class_name = request.POST.get('class_name', None)
		id_name = request.POST.get('id_name', None)
		new_url = URL(url=hyperlink, main_tag=tag_name, sub_tag=sub_tag_name, class_name=class_name, id_name=id_name, get_date=timezone.now())
		new_url.save()
		return HttpResponseRedirect('/scrape/{0}'.format(new_url.id))
	else:
		return render(request, 'scrape/add_urls.html')