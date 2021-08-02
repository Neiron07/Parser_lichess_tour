import requests
import sys
from bs4 import BeautifulSoup
import urllib.request
import json

def links(url):
    #Парсим турнир с клуба
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    arr1=[]
    
    for el in soup.select('.enterable'):
                    url_more = el.select_one('a').get('href')
                    if url_more[1] == 't':
                        arr1.append(str(url_more))
    

    prize_word=["Взнос ", '₽', '$', 'prize fond', 'rub', "1st plaсe", 'fee', 'руб.', 'ПФ', 'Призовой Фонд', 'prize tournament']
    prizearr=[]

    for i in arr1:
        response = requests.get("https://lichess.org/api"+str(i))
        todos = json.loads(response.text)
        
        if "description" in todos:
            for j in todos['description']:
                if j in prize_word:
                    prizearr.append(i)



    newlist = sorted(set(prizearr), key=lambda x:prizearr.index(x))
    file=open(f'D:\data_file.json', 'w')
    file.write("Prize tournament:"+"\n")
    file.close()


    for links in newlist:
        response = requests.get("https://lichess.org/api"+str(links))
        todos = json.loads(response.text)
        with open(f'D:\data_file.json', 'a', encoding="utf-8") as outfile: #Путь к json file
            json.dump(
              {
              "Tournaments Name" : todos['fullName'],
              "Created By" : todos['createdBy'],
              "System" : todos['system'],
              "Number of players" : todos['nbPlayers'],
              "Time tournament" : todos['minutes'],
              "Variant" : todos['variant'],
              "Berserk " : todos['berserkable'],
              "Condition " : todos['verdicts']['list'],
              "Date " : todos['startsAt'],
              "Link " : "https://lichess.org/tournament/"+str(todos['id']),
              "Description and prize" : todos['description'], 
              }, outfile, ensure_ascii=False, indent=4)
        
       


if __name__ == "__main__":
    
    links('https://lichess.org/team/chesslandia')
    
