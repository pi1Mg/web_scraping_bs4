from bs4 import BeautifulSoup


def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(), 'lxml')

#  .contents        -- returns us only direct children of the said tag
body = soup.body
children = [child for child in body.contents if child != '\n']
print(children)
print(len(children))


#  .descendants     -- returns all the children from a tag -- generator
for index, child in enumerate(soup.head.descendants):
    print("{}: {}".format(index, child if child != '\n' else 'new line'))
