from bs4 import BeautifulSoup


def file_read():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(file_read(), 'lxml')

title = soup.title
parent = title.parent
# print(parent.name)      # .name -- tag's name

#  .parent
p = soup.p
print(p.parent.name)

#  html
html = soup.html
print(type(html.parent))

#  soup
print(soup.parent)
