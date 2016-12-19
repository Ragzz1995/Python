import urllib
import xml.etree.ElementTree as ET
xml = urllib.urlopen('http://python-data.dr-chuck.net/comments_341016.xml').read()
tree = ET.fromstring(xml)
r = tree.findall('comments/comment')
sum = 0
for j in r:
	sum = sum + int(j.find('count').text)

print sum
