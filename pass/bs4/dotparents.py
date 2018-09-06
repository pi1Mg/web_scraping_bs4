from bs4 import BeautifulSoup


def file_read():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(file_read(), 'lxml')

#  .parents     -- returns a list (generator) of parents
link = soup.a
# print(link.parents)
#  give me a full path of names from tag to the top
print([parent.name for parent in link.parents])
