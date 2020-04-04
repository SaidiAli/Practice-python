import requests

req = requests.get('https://www.nytimes.com/')
res = req.text
print(res)