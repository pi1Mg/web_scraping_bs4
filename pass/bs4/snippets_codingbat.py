# import sys
import time
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
user_agent = UserAgent()
start_time = time.time()


def save_url(url_1, file_name, mode='a'):
    page = requests.get(url_1, headers={'user-agent': user_agent.chrome}).content
    with open(file_name, mode) as file:
        file.write(page.decode('utf-8')
                   if type(page) == bytes
                   else file.write(page))
    return "Saving file: " + file_name


def read_file(file_name):
    with open(file_name, 'r') as file:
        data_1 = file.read()
    return data_1


def make_soup(url_2):
    page = requests.get(url_2,
                        headers={'user-agent': user_agent.chrome}).content
    medley = BeautifulSoup(page, 'lxml')
    return medley

# print(save_url('https://codingbat.com/java', 'codingbat_java.txt'))

url_prefix = r'https://codingbat.com'
soup = BeautifulSoup(read_file('codingbat_java.txt'), 'lxml')
sections = {}  # key: section name, value: [tasks(dict), task_link]
#  tasks -> key: task_name, value: [task_text, task_text_link]

#  Get main sections of exercises: Warmup_1 _2 etc
# Warmup_1 -> sleepIn -> text
# Warmup_1 -> {'sleepIn': 'text', 'dif21': 'text'}
# {'Warmup_1': {'sleepIn': 'text', 'dif21': 'text'},
#  'Warmup_2': {'stringX': 'text', 'doubleX': 'text'}}


test = {'Warmup_1': [{'sleepIn': ['task_text_link1', 'text1'], 'dif21': ['task_text_link2', 'text2']}, 'section_link1'],
        'Warmup_2': [{'stringX': ['task_text_link1', 'text1'], 'doX': ['task_text_link2', 'text2']}, 'section_link2']}

# print(test)
# print(test['Section_1'][0]['sleepIn'][1])

section_divs = soup.find_all('div', attrs={'class': 'summ'})
data = {}
s = list()
'''
for section_div in section_divs:
    s.append([var.text for var in make_soup(url_prefix + section_div.a['href']).find_all('div', class_='indent')])
    # with open('buffer.txt', 'a') as file:
    #     file.write('\n'.join((str(red) for red in s)))
    # data = {section_div.a.text: [[task_div.a.text for task_div in s], url_prefix + section_div.a['href']]}
    # i need to go into every section_linkX and populate task_text_linkX
    # and again navigate to task_text_linkX to get textX
    print(s)
    pass
# print(make_soup(r'http://google.com'))
'''

#  Name of sections
section_names = [name.a.text for name in section_divs]

#  URL for each section
#  TODO: join into same loop (section names and urls)
section_urls = [url_prefix + section_url.a['href'] for section_url in section_divs]

#  Make a soup for each section URL?
#  I will just make one big soup, from 1 text file and than extract data
'''
big_soup_body = ''
for section_div in section_divs:
    for url in section_urls:
        big_soup_body += str(make_soup(url).body) + '\n'

    with open('big_soup_body.txt', 'w') as f:
        f.write(big_soup_body)
'''

#  Last thing that I tried on main quest

soup_a = BeautifulSoup(read_file('big_soup_tasks.txt'), 'lxml')
tasks_divs = soup_a.find_all('div', class_='indent')
task_names = [name.table.tr.td.a.text for name in tasks_divs]
task_links = [url_prefix + link.table.tr.td.a['href'] for link in tasks_divs]

'''
big_soup_body = ''
i = 0
for url in task_links:
    i += 1
    big_soup_body += str(make_soup(url)) + '\n'
    print('{}: adding content from {} to a big soup text'.format(i, url))
    if i == 5:
        break

with open('big_soup_tasks_text.txt', 'w', encoding='utf-8') as f:
    f.write(big_soup_body)
    print('writing file: {}, size: {}'.format(f.name, f.tell()))
'''

for i, task_link in enumerate(task_links):
    print(i, task_link)





print("--- running %s seconds ---" % (time.time() - start_time))