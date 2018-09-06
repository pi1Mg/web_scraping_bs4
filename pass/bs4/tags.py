from bs4 import BeautifulSoup


def read_file():
    file = open('tags.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(), 'lxml')
# print(soup.prettify())

#  Accessing tags
meta = soup.meta

# div = soup.div
# print(div)

#  tag methods
"""
name
-- attributes
.get() method
dictionary
"""
# print(meta.get('charset'))
#  I can also read this attribute as a dictionary
# print(meta['charset'])

#  Modify attributes
body = soup.body
print(body['style'])
body['style'] = 'some style'
print(body['style'])

#  Multi valued attributes
print(body['class'])
