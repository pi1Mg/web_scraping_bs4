from bs4 import BeautifulSoup


def file_read():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(file_read(), 'lxml')

body = soup.body

#  contents - html
# print(soup.html.contents)

#  .previous_sibling
#  Doing twice because of '\n' char in file
print(body.previous_sibling.previous_sibling)


