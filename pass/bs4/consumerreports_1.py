import re
from bs4 import BeautifulSoup


def read_file():
    file = open('consumer_reports.txt')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(), 'lxml')

#  <div class="crux-body-copy">
all_divs = soup.find_all('div', attrs={'class': "crux-body-copy"})

#  seems that i can use .text and .string interchangeably
for div in all_divs:
    # print(div.text.strip())
    # print(div.a.string.strip())
    pass

products = [div.a.text.strip() for div in all_divs]
# print(products)
for product in products:
    # print(product)
    pass









