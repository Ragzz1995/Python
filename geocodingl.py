import urllib
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'


address = raw_input('Enter location: ')
    

url = serviceurl + urllib.urlencode({'address': address,'key':'Your google API key'})

uh = urllib.urlopen(url)
data = uh.read()
js = json.loads(str(data))
print json.dumps(js["results"][0]["geometry"]["location"]["lat"],indent=4)
print json.dumps(js["results"][0]["geometry"]["location"]["lng"],indent=4)

