import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


ua = UserAgent()
headers = {'user-agent': ua.chrome}
google_resp_obj = requests.get('https://www.google.com', headers=headers)

soup = BeautifulSoup(google_resp_obj.content, 'lxml')
print(soup.prettify())
