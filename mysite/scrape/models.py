from django.db import models
from bs4 import BeautifulSoup
import requests


def page(hyper, tag=None):
	req_headers = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.8',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
		}
	source = requests.get(hyper,headers=req_headers).text
	soup = BeautifulSoup(source, 'lxml')
	table = soup.find_all(tag)
	if len(table) > 1:
		array = []
		for item in table:
			if tag == 'a':
				array.append(item['href'])
			if tag != 'a':
				array.append(item.text)
		return array
	if len(table) == 1:
		return table

class URL(models.Model):
	tag = models.CharField(max_length=7, default='div')
	url = models.URLField(max_length=200)
	get_date = models.DateTimeField('date scrapped')
	def __str__(self):
		return self.url
		
	def get_data(self):
		return page(self.url, self.tag)
		
		
		
		