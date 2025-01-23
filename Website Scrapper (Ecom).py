# Scrap Data form a Ecom Website 

import requests
from bs4 import BeautifulSoup 
import pandas as pd


data = {'Title': [], 'Price': []}
   
url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=headers)  

soup = BeautifulSoup(r.text, 'html.parser')

divs = soup.find_all(class_='KzDlHZ')
for div in divs:
    print(div.text)
    data["Title"].append(div.text)

divs2 = soup.find_all(class_='Nx9bqj')

for div in divs2:
    print(div.text)
    data["Price"].append(div.text)
    if len(data['Price']) == len(data['Title']):
        break

df = pd.DataFrame.from_dict(data)
df.to_excel("Data.xlsx", index=False)





