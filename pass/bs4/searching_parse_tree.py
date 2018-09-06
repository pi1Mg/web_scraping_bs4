import re
from bs4 import BeautifulSoup


def file_read():
    file = open('three_sisters.html')
    data = file.read()
    return data

soup = BeautifulSoup(file_read(), 'lxml')

#  most popular methods
#  find()
#  find_all()

#  Kinds of filters we can use to retrieve tags
#  - filters sent as parameter to find/find_all methods

#  string
# print(soup.find_all('a'))

#  Regular expression
#  tag names start with b
regex_b = re.compile(r'^b')

for tag in soup.find_all(regex_b):
    # print(tag.text)
    pass

#  tag names contain t
regex_t = re.compile(r't')

for tag in soup.find_all(regex_t):
    # print(tag.name)
    pass

#  list (give a list as a parameter for bs4 find_all method)
#  give me all b and a tags
for tag in soup.find_all(['a', 'b']):
    # print(tag.name)
    pass

#  function
def has_class(tag):
    return tag.has_attr('class')

for tag in soup.find_all(has_class):
    print(tag.name)




