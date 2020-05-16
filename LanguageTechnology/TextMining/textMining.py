#Emmi Lahtisalo

'''Mining Weather Forecasts'''

##########################

from urllib import request
from bs4 import BeautifulSoup

# Choosing Helsinki area
url = "http://www.foreca.fi/Finland/Helsinki"
html = request.urlopen(url).read()
soup = BeautifulSoup(html, "lxml")

# Title
title = soup.find("title").get_text(" ", strip=True) 

# Forecast time
time = soup.find("div", attrs={"style": "float: left; width: 95%;"}).strong.get_text(" ", strip=True)

# Current temperature
currentCelsius = soup.find("span", attrs={"class": "cold txt-xxlarge"}).get_text(" ", strip=True)

# Current weather conditions
currentWeather = soup.find("div", attrs={"class": "right txt-tight"}).get_text("\n", strip=True)

# Three day forecast
ThreeDayForecast = soup.find_all("div", attrs={"class": "c2_a"})

# Hottest and coldest temperatures on Earth
hottest = soup.find_all("div", attrs={"class": "triviarow"})[0].text.strip()
coldest = soup.find_all("div", attrs={"class": "triviarow"})[3].text.strip()
    

# Prints

print(title + "\nForecast time: " + time 
      + "\nTemperature: " + currentCelsius + "\n\n" + currentWeather)

print("\nHottest place on Earth: " + ' '.join(hottest.split()) 
      + "\nColdest place on Earth: " + ' '.join(coldest.split()) 
      + "\n\nThree Day Forecast:")

for div in ThreeDayForecast:
    print("\n" + div.get_text("\n", strip=True))

    
# The problem with this execution is that even minor changes to the layout of the site will mess up the results.
