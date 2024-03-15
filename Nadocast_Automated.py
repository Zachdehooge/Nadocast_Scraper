import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from datetime import datetime

now = datetime.now()

#Uncomment print statements to debug time constraints
month = now.strftime("%m")
#print("d3 =", month)

day = now.strftime("%d")
#print("d3 =", day)

year = now.strftime("20%y")
#print("d3 =", year)

timeNow = now.strftime("%H")
#print("d3 =", timeNow)

if 0 <= int(timeNow) <= 13:
    timeNow = 0
elif 14 <= int(timeNow) <= 18:
    timeNow = 12
elif 19 <= int(timeNow) <= 23:
    timeNow = 18
else:
    print("(-) No Nadocast Data To Fetch // Check If Statement Set For Constraints Covering Current Time: {0}".format(timeNow))

#URL Structure 
#url = "http://data.nadocast.com/202403/20240315/t0z/"

url = "http://data.nadocast.com/{2}{1}/{2}{1}{0}/t{3}z/".format(day, month, year, timeNow)


#If there is no such folder, the script will create one automatically
folder_location = r'C:\\Nadocast\\{1}_{0}_{2}_{3}z'.format(day, month, year, timeNow)
if not os.path.exists(folder_location):os.makedirs(folder_location)

response = requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")     
for link in soup.select("a[href$='.png']"):
    #Name the png files using the last portion of each link which are unique in this case
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)
