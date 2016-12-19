import urllib
from bs4 import BeautifulSoup
import re
import subprocess
import time
while True:
	html = urllib.urlopen('http://www.accuweather.com/en/in/coimbatore/206673/current-weather/206673')
	soup = BeautifulSoup(html)
	x = soup.find('span',{'class':'large-temp'})
	m1 = 'Coimbatore temperature is '+ re.findall('[0-9]+',str(x))[0]



	html = urllib.urlopen('https://www.timeanddate.com/worldclock/india/coimbatore')
	soup = BeautifulSoup(html)
	x = soup.find('div',{'class':'main-content-div'})
	tim = x.find_all('span')
	k = re.findall('[0-9]+:[0-9]+:[0-9]+',str(tim[0]))
	m2 =  'The time is ' + k[0]


	subprocess.Popen(['notify-send', m1,m2])
	time.sleep(30)
