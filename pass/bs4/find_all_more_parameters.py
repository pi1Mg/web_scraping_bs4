import re
from bs4 import BeautifulSoup


def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(), 'lxml')

#  Signature: find_all(name=None, attrs:dict={}, recursive:bool=True,
#  text=None, limit=None, **kwargs)

#  string (text) parameter
regex_text_elsie = re.compile(r'Elsie')
tag_elsie = soup.find_all(text=regex_text_elsie)
# print(tag_elsie)

regex_text_story = re.compile(r'story')
tag_story = soup.find_all(text=regex_text_story)
# print(tag_story)

#  **kwargs arguments
#  to write class attribute of a tag -> use class_ (reserved keyword in py)
tags_via_class = soup.find_all(class_='sister')
# for tag in tags_via_class:
#     print(tag)

#  recursive parameter
title = soup.find_all('title', recursive=True)
print(title)

#  find() returns a signe object if found, if there are more, returns first
#  Signature: find_all(name=None, attrs:dict={}, recursive:bool=True,
#  text=None, **kwargs) -> like find_all() with limit=1