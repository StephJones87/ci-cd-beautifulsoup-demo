import requests
from bs4 import BeautifulSoup

def get_title(url):
    response = requests.get(url)
    print(response.status_code)
    print(response.text[:500])  # just show a snippet of HTML
    soup = BeautifulSoup(response.text, "html.parser")
    h1_tag = soup.find("h1")
    return h1_tag.text.strip() if h1_tag else None