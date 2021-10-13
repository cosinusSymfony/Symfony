import requests

r = requests.get('https://python.org')
print(r.status_code)
print(r.content)
print(r.cookies)
print(b'Python is a programing language ' in r.content)
