from bs4 import BeautifulSoup


def file_read():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(file_read(), 'lxml')

p = soup.body.p

#  .next_siblings
for sibling in p.next_siblings:
    # print(sibling.name if sibling != '\n' else "New line found!")
    pass

#  .previous_siblings
for sibling in p.previous_siblings:
    print(sibling.name if sibling != '\n' else "New line found!")
