from django.db import models
from bs4 import BeautifulSoup
import requests

def do_if_sub(table, sub_tag):
	for part in table:
		leg = part.find_all(sub_tag)
		if len(leg) > 1:
			array = []
			for splinter in leg:
				if sub_tag == 'a':
					array.append(splinter['href'])
				if sub_tag != 'a':
					try:
						array.append(splinter.text)
					except:
						array.append(splinter)
			return array
		if len(leg) == 1:
			try:
				return leg.text
			except:
				return leg

def do_no_sub(table, main_tag):
	if len(table) > 1:
		array = []
		for item in table:
			if main_tag == 'a':
				array.append(item['href'])
			if main_tag != 'a':
				try:
					array.append(item.text)
				except:
					array.append(item)
		return array
	if len(table) == 1:
		try:
			return table.text
		except:
			return table
			
def page(hyper, main_tag=None, sub_tag=None, class_name=None, id_name=None):
	req_headers = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.8',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
		}
	source = requests.get(hyper,headers=req_headers).text
	soup = BeautifulSoup(source, 'lxml')
	if class_name == '' and id_name == '':
		table = soup.find_all(main_tag)
		if sub_tag == '':
			return do_no_sub(table, main_tag)
		if sub_tag != '':
			return do_if_sub(table, sub_tag)
				
	if class_name and id_name == '':
		table = soup.find_all(main_tag, class_=class_name)
		if sub_tag == '':
			return do_no_sub(table, main_tag)
		if sub_tag != '':
			return do_if_sub(table, sub_tag)
			
	if class_name == '' and id_name:
		table = soup.find(main_tag, id=id_name)
		if sub_tag == 'a':
			array = []
			leg = table.find_all(sub_tag)
			for splinter in leg:
				array.append(splinter['href'])
			return array
		if sub_tag != 'a':
			return [table.text]

class URL(models.Model):
	main_tag = models.CharField(max_length=7, default='div')
	sub_tag = models.CharField(max_length=7, default='a')
	class_name = models.CharField(max_length=100, default='')
	id_name = models.CharField(max_length=100, default='')
	url = models.URLField(max_length=200)
	get_date = models.DateTimeField('date scrapped')
	def __str__(self):
		return self.url
		
	def get_data(self):
		return page(self.url, self.main_tag, self.sub_tag, self.class_name, self.id_name)
		
		
		
		