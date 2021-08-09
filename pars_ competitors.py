import requests
import sys
from bs4 import BeautifulSoup
import urllib.request
import json

def arenum(url):
	resp = requests.get(url)
	soup = BeautifulSoup(resp.content, 'html.parser')
	info_tour=[]
	info_tour1=[]

	for el in soup.select('a'):
		arr=el.get('href')
		info_tour.append(arr)

	for links in info_tour:
		if len(links) > 30:
			info_tour1.append('https://arenum.games'+links)

  del info_tour1[-2]
	del info_tour1[-1]

	for info in info_tour1:
		print(info)
		



def liquipedia(url, url2, url3):
	#Brawl Stars
	links_brawlstars=[]
	headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
	resp = requests.get(url, headers=headers)
	soup = BeautifulSoup(resp.content, 'html.parser')
	ar=soup.find_all('div',{'class':'divRow tournament-card-premier'})
	for el in ar:
		ar1=el.find('b')
		for j in ar1:
			links = j.get('href')
			links_brawlstars.append('https://liquipedia.net'+links)
			

	#CLASH ROYALE
	links_clash=[]
	resp1 = requests.get(url2, headers=headers)
	soup1 = BeautifulSoup(resp1.content, 'html.parser')
	html=soup1.find_all('div', {"class":"divRow"})	
	for elem in html:
		v=elem.find('b')
		for ver2 in v:
			links1=ver2.get('href')
			links_clash.append('https://liquipedia.net'+links1)

	
	#PUBG
	links_pubgmob=[]
	resp2 = requests.get(url3, headers=headers)
	soup2 = BeautifulSoup(resp2.content, 'html.parser')
	stylehtml=soup2.find('style')
	html2=soup2.find_all('div', {"class":"divRow"})
	for elem2 in html2:
		v2=elem2.find('b')
		for ver3 in v2:
			links2=ver3.get('href')
			links_pubgmob.append('https://liquipedia.net'+links2)


	
	list_brawl=links_brawlstars[:20]
	list_clash=links_clash[:4]
	list_pubgmob=links_pubgmob[:7]

	for pubgmob in list_pubgmob:
		print(pubgmob)
	for brawlstars1 in list_brawl:
		print(brawlstars1)
	for clashroyale1 in list_clash:
		print(clashroyale1) 



if __name__ == '__main__':
	liquipedia('https://liquipedia.net/brawlstars/A-Tier_Tournaments', 'https://liquipedia.net/clashroyale/Tier_3_Team_Tournaments', 'https://liquipedia.net/pubg/A-Tier_Tournaments/Mobile')
	arenum('https://arenum.games/ru/tournaments/list/9TPUvluOEemGR9ZjvYc9kw#_jSIydpETWyEdV10XfE68w')
	arenum('https://arenum.games/ru/tournaments/list/9TPgOluOEemGR9ZjvYc9kw')
	#cyberhero('https://cyberhero.tele2.ru/cups')
