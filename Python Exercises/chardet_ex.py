import urllib.request
from chardet.universaldetector import UniversalDetector

usock = urllib.request.urlopen('http://yahoo.co.jp/')
detector = UniversalDetector()
for line in usock.readlines():
    detector.feed(line)
    if detector.done: break
detector.close()
usock.close()
print (detector.result, '\n')

'''
import glob

detect = UniversalDetector()
for file in glob.glob('./CSV/*.csv'):
	print(file)
	detect.reset()
	for line in file(file, 'rb'):
		detect.feed(line)
		if detect.done:
			detect.close()
			print(detect.result)
'''