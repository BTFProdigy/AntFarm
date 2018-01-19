from collections import namedtuple
import re

my_py = 'foo'
print(my_py)

Color = namedtuple('Color', ['red', 'blue', 'green'])
color = Color(55,150,255)

print(color.red)


test_string = 'my test string dept, alpha'

#pattern looks for 0 or more 
#whitespace charachters, returns list 
print(re.split(r'\s*', 'Here are some words'))

#same as above but includes the spaces in the list
print(re.split(r'(\s*)', 'Here are some words'))

#split by s any number of s. so the
print(re.split(r'(s*)', 'Here are some words sss'))

#split by a-f splits through the range a,b,c,d,e,f
print(re.split(r'[a-f]', 'sydufiksgdhfgj'))

#splits by range lower and upper case
print(re.split(r'[a-fA-F]', 'KJHGFefghjNSDFGYtresCvb'))

#looking for an address
#\d digits \D non-digits \S non-space
#\d{1,5} find a string of digits in range 1-5
#\s look for a space, \w+ look for at least one letter
#\. look for a regular period
print(re.findall(r'\d{1,3}\s\w+\s\w+\.','finqwen324 main st.iewasd'), 
		re.I|re.M)