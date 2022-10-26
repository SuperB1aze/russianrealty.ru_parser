import requests
from bs4 import BeautifulSoup

url = "https://www.russianrealty.ru/%D0%9F%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80/"
headers = {
    "Accept": 
       "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
   "User-Agent":
	    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
}

req = requests.get(url, headers=headers)
src = req.text
print(src)

with open("index.html", "w") as file:
   file.write(src)

with open("index.html", "r") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
all_appartments_hrefs = soup.find_all("div", {"class": "hproduct"})

all_appartments_dict = {}
for div in all_appartments_hrefs:
    item_name = div.find('a').text
    item_name = item_name.replace("&sup2", "2")
    item_href = "https:" + div.find('a').get('href')

    item_price = div.find('span').text
    item_adress = div.find('p', class_ = "adr").text

    in_point = item_adress.index("«")
    item_adress = item_adress[0:in_point]

    all_appartments_dict[item_name] = [item_href, item_price, item_adress]

print(all_appartments_dict)