from bs4 import BeautifulSoup


def file_read():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(file_read(), 'lxml')

body = soup.body
p = soup.body.p

#  body - contents
# print(body.contents)

#  .next_sibling
#  Because of '\n' from file, I have to use .next_sibling twice
print(p.next_sibling.next_sibling)
