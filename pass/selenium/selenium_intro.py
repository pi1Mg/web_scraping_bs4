from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup


#  Make a webdriver object --> point to driver path
driver = webdriver.Chrome('C:\est\chromedriver_win32\chromedriver.exe')

#  Open some page using get method
driver.get('https://google.com')
soup = BeautifulSoup(driver.page_source, 'lxml')
print(soup.prettify())


#  Always close webdriver object
driver.close()

