from bs4 import BeautifulSoup


def read_file():
    file = open('intro_to_soup_html.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(), 'lxml')

#  Navigable strings


#  string inside a tag  - .string
# print(soup.title.string)

#  .replace_with("") function
# title = soup.title
# title.string.replace_with("Title has been changed")
# print(title)
