#Emmi Lahtisalo, 014163276

'''Assignment 3.3'''

##########################

from urllib import request
from bs4 import BeautifulSoup

url = "http://www.foreca.fi/Finland/Helsinki"
html = request.urlopen(url).read()
soup = BeautifulSoup(html, "lxml")

#Otsikko
title = soup.find("title").get_text(" ", strip=True) 

#Havaintoaika
time = soup.find("div", attrs={"style": "float: left; width: 95%;"}).strong.get_text(" ", strip=True)

#T�m�n hetken l�mp�tila
currentCelsius = soup.find("span", attrs={"class": "cold txt-xxlarge"}).get_text(" ", strip=True)

#T�m�n hetken tarkemmat s��tiedot
currentWeather = soup.find("div", attrs={"class": "right txt-tight"}).get_text("\n", strip=True)

#Kolmen p�iv�n ennuste
ThreeDayForecast = soup.find_all("div", attrs={"class": "c2_a"})

#Kuumimmat ja kylmimm�t mitatut l�mp�tilat maapallolla
hottest = soup.find_all("div", attrs={"class": "triviarow"})[0].text.strip()
coldest = soup.find_all("div", attrs={"class": "triviarow"})[3].text.strip()
    

#Tulosteet haetuille tiedoille

print(title + "\nHavaintoaika: " + time + "\nL�mp�tila: " + currentCelsius + "\n\n" + currentWeather)

print("\nKuumin mitattu l�mp�tila maailmalla: " + ' '.join(hottest.split()) + "\nKylmin mitatttu l�mp�tila maailmalla: " + ' '.join(coldest.split()) + "\n\nKolmen p�iv�n ennuste:")

for div in ThreeDayForecast:
    print("\n" + div.get_text("\n", strip=True))


#Toivottavasti ��kk�set ei aiheuta mit��n ongelmia.