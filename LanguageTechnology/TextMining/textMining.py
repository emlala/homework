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

#Tämän hetken lämpötila
currentCelsius = soup.find("span", attrs={"class": "cold txt-xxlarge"}).get_text(" ", strip=True)

#Tämän hetken tarkemmat säätiedot
currentWeather = soup.find("div", attrs={"class": "right txt-tight"}).get_text("\n", strip=True)

#Kolmen päivän ennuste
ThreeDayForecast = soup.find_all("div", attrs={"class": "c2_a"})

#Kuumimmat ja kylmimmät mitatut lämpötilat maapallolla
hottest = soup.find_all("div", attrs={"class": "triviarow"})[0].text.strip()
coldest = soup.find_all("div", attrs={"class": "triviarow"})[3].text.strip()
    

#Tulosteet haetuille tiedoille

print(title + "\nHavaintoaika: " + time + "\nLämpötila: " + currentCelsius + "\n\n" + currentWeather)

print("\nKuumin mitattu lämpötila maailmalla: " + ' '.join(hottest.split()) + "\nKylmin mitatttu lämpötila maailmalla: " + ' '.join(coldest.split()) + "\n\nKolmen päivän ennuste:")

for div in ThreeDayForecast:
    print("\n" + div.get_text("\n", strip=True))


#Toivottavasti ääkköset ei aiheuta mitään ongelmia.