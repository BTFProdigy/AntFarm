import re
import urllib
try:
	import urllib.request
except:
	pass

sites = 'google yahoo cnn msn'.split()

for s in sites:
	print('Searching: ' + s)
	try:
		u = urllib.urlopen('http://' + s + 'com')
	except:
		u = urllib.request.urlopen('http://' + s + '.com')
	text = u.read()
	title = re.findall(r'<title>+.*</title>+',
		str(text), re.I|re.M)

	print(title[0])