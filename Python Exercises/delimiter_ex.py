import glob
import re
from collections import Counter

for filename in glob.glob('./CSV/*.csv'):
	with open(filename, 'rb') as f:
		line = f.readline()
		c = Counter(line.decode())
		print(line.count(b','))
		x = c.most_common()
		print(max(x))
