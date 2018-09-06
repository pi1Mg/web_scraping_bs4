from bs4 import BeautifulSoup


def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(), 'lxml')

#  Signature: find_all(name=None, attrs:dict={}, recursive:bool=True,
#  text=None, limit=None, **kwargs)

#  name parameter (regex object, string, True, function)
a_tags = soup.find_all('a')

#  attrs parameter (dictionary)
attr = {'class': 'sister', 'id': 'link1'}
first_a = soup.find_all('a', attrs=attr)
# print(first_a)

#  limit parameter
a_tags_limit = soup.find_all('a', limit=2)
print(a_tags_limit)



