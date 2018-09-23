from selenium import webdriver
from time import sleep
import time
start_time = time.time()


web_driver_path = 'C:\est\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(web_driver_path)

#  Open instagram
driver.get(r'https://www.instagram.com')
sleep(2)

#  Click on login button
login_button = driver.find_element_by_link_text('Log in')
login_button.click()
sleep(5)

#

driver.close()
print("--- running %s seconds ---" % (time.time() - start_time))
