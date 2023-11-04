import requests as re

response = re.get("https://www.pokemon.com/us")
html = response.text
print(html)
