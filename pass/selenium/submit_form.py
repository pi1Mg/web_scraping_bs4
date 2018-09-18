from selenium import webdriver
from time import sleep


#  Make a webdriver object --> point to driver path
driver = webdriver.Chrome('C:\est\chromedriver_win32\chromedriver.exe')

#  Open some page using get method
driver.get('https://google.com')

#  Find search bar using id
search_bar = driver.find_element_by_id('lst-ib')

#  Input data
search_bar.send_keys('I want to learn web scraping')

#  Submit the form
search_bar.submit()
sleep(5)

#  Always close webdriver object
driver.close()

