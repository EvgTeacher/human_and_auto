import requests
import fake_useragent

url = 'https://allo.ua/ua/roboty-pylesosy/'

user = fake_useragent.UserAgent().random
print(user)

# response = requests.get(url)
# print(response.text)