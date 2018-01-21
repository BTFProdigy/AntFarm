import urllib.request
from chardet.universaldetector import UniversalDetector

usock = urllib.request.urlopen('http://yahoo.co.jp/')
detector = UniversalDetector()
for line in usock.readlines():
    detector.feed(line)
    if detector.done: break
detector.close()
usock.close()
print (detector.result)


import glob

detector = UniversalDetector()
for filename in glob.glob('./CSV/*.csv'):
    print ('\n' + filename.ljust(60)),
    detector.reset()
    for line in open(filename, 'rb'):
        detector.feed(line)
        if detector.done: break
    detector.close()
    print (detector.result)

