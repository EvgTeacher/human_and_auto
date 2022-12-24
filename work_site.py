import requests
import fake_useragent
from bs4 import BeautifulSoup

url = 'https://allo.ua/ua/roboty-pylesosy/'

user = fake_useragent.UserAgent().random
# print(user)
headers = {"user-agent": user}

response = requests.get(url, headers=headers)
# print(response.text)
soup = BeautifulSoup(response.text, "lxml")
# print(soup)

all_product = soup.find('div', class_='products-layout__container products-layout--grid')

product_list = all_product.find_all('div', class_='product-card')
# print(product_list[0])

for i in range(len(product_list)):
    product_title = product_list[i].find('a', class_='product-card__title')
    price = product_list[i].find("div", class_='v-pb__cur discount')
    url_product = product_list[i].find("div", class_ = 'product-card__content')
    print(product_title.text, price.text)
    print(url_product.text)

    # with open('myproduct.txt', 'a', encoding='utf-8') as file:
    #     file.write(f"{product_title.text}")