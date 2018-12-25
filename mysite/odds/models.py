from django.db import models

# Create your models here.
from bs4 import BeautifulSoup
import requests
import csv
import re

def player_lookup(name, opp):
	if name == "Justin Wong":
		name = "JWong"
	if opp == "Justin Wong":
		opp = "JWong"
	if name == "Daigo":
		name = "Daigo_Umehara"
	if opp == "Daigo":
		opp = "Daigo_Umehara"
	array = []
	source = requests.get('https://liquipedia.net/fighters/{0}/Results'.format(name)).text
	soup = BeautifulSoup(source, 'lxml')
	table = soup.find('table')
	for section in table.find_all('tr'):
		for data in section.find_all('td'):
			links = data.find_all('a')
			for link in links:
				if link.text == opp:
					data = section.text
					data = data.replace('\n', ' ').replace('B3', '').replace('A3', '').replace('A1','').replace('A2','').replace('A9','').replace('\xa0','')
					date = re.search(r'\d{4}-\d{2}-\d{2}',data).group()
					score = re.search(r'\d: \d',data).group()
					score = score.replace(' ','')
					try:
						place = re.search(r'\d{1,2} - \d*[a-z]*',data).group()
						place = place.replace(' ','')
					except:
						place = re.search(r'\d[a-z]{2}', data).group()
					tourney = re.search(r'   .*?   ', data).group()
					tourney = tourney.replace('   ','')
					game_stats = [date, score, place, tourney]
					array.append(game_stats)
	return array
				
def get_stats(player, opp):
	past_games = player_lookup(player, opp)
	total_majors = len(past_games)
	player_wins = 0
	for game in past_games:
		if int(game[1][0]) > int(game[1][2]):
			player_wins += 1
	return past_games, total_majors, player_wins
	
	
class Pairs(models.Model):
	player = models.CharField(max_length=10, default="Tokido")
	opp = models.CharField(max_length=10, default="Momochi")
	
	def __str__(self):
		return self.player
		
	def get_data(self):
		return get_stats(self.player, self.opp)
	