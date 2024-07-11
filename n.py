import requests
r=requests.get("https://meme-api.com/gimme")
d=r.json()
print(d['preview'])