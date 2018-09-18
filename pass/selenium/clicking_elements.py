from selenium import webdriver
from time import sleep


#  Make a webdriver object --> point to driver path
driver = webdriver.Chrome('C:\est\chromedriver_win32\chromedriver.exe')

#  Open instagram.com using get method
driver.get('https://instagram.com')
sleep(5)
login_button = driver.find_element_by_link_text('Log in')
login_button.click()
sleep(5)



#  Always close webdriver object
driver.close()

