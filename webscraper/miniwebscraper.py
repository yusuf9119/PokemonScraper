import requests
import time
from bs4 import BeautifulSoup

url = "https://www.pokemon.com/us"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')  # Use 'html.parser' instead of 'html parser'
        #scraping code here
    else:
        print("Failed to retrieve it. Status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("An error has occurred:", e)

time.sleep(1)