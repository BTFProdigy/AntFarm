import requests

r = requests.Session()
u = r.get('https://api.github.com/events')

print(u.text)