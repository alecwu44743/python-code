import requests
from bs4 import BeautifulSoup

url = "https://travel.ettoday.net/category/桃園/"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

titles = soup.find_all("h3", itemprop="headline")
for title in titles:
    print(title.select_one("a").getText())
    
# //*[@id="ft"]/tbody[2]