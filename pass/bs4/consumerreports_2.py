import re
from bs4 import BeautifulSoup


def read_file():
    file = open('consumer_reports.txt')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(), 'lxml')

products = {}  # key: product name, value: link

product_names = [div.a.text.strip() for div in
                 soup.find_all('div', attrs={'class': 'crux-body-copy'})]
# product_names = [div.a.text.strip() for div in soup.find_all('div', "crux-body-copy")] -> works also without attrs
for p in product_names:
    # print(p)
    pass

links = [div.a['href'] for div in soup.find_all('div', attrs={'class': 'crux-body-copy'})]
for l in links:
    # print(l)
    pass


products = {div.a.text.strip(): div.a['href'] for div in
            soup.find_all('div', attrs={'class': 'crux-body-copy'})}


for key, value in products.items():
    print(key, ' --> ', value)












