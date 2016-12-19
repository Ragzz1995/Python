import urllib
import json
url = 'https://translation.googleapis.com/language/translate/v2?'
add = urllib.urlencode({'key':'AIzaSyByyfmD2OjN6vyg_dQAOT0C2IFujt08GpE','target':'Tamil','q':raw_input('Enter Text:')})
final = url + add
f = urllib.urlopen(final)
print f.read()

