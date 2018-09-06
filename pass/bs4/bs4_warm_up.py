from bs4 import BeautifulSoup
import requests

url = "https://www.emmi.rs/"
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

#  Getting the web page, creating a Response object.
response = requests.get(url, headers=headers)

#  Extracting the source code of the page
data = response.text

#  Passing the source code to Beautiful Soup to create a
#  BeautifulSoup object for it
soup = BeautifulSoup(data, 'html.parser')

#  Extracting all the <a> tags into a list.
tags = soup.find_all('a')

#  Extracting URLs from the attribute href in the <a> tags
for tag in tags:
    print(tag.get('href'))
