import urllib
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
html = urllib.urlopen(url)

soup = BeautifulSoup(html)

right_table = soup.find('table',{'class':'wikitable sortable plainrowheaders'})
a = []
b = []
c = []
d = []
e = []
f = []
g = []
print soup.find_all(text=True)
for row in right_table.find_all('tr'):
	cells = row.find_all('td')
	states = row.find_all('th')
	if len(cells) == 6:
		print cells[0]
		a.append(cells[0].find(text=True))
		b.append(states[0].find(text=True))
		c.append(cells[1].find(text=True))
		d.append(cells[2].find(text=True))
		e.append(cells[3].find(text=True))
		f.append(cells[4].find(text=True))
		g.append(cells[5].find(text=True))


