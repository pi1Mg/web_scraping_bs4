from selenium import webdriver
from time import sleep
import time
start_time = time.time()


web_driver_path = 'C:\est\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(web_driver_path)
'''
#  Open instagram
driver.get(r'https://www.instagram.com')
sleep(2)

#  Click on login button
xpath = "//span[@id='react-root']//p[@class='izU2O']/a"
login_button = driver.find_element_by_xpath(xpath)
login_button.click()
sleep(5)
'''
#  Google search via xpath
driver.get(r'https://google.com')
sleep(2)

# click on search bar
#  directly -> //input[@id='lst-ib']
xpath_search_bar = "//div[@id='gs_lc0']/input"
search_bar = driver.find_element_by_xpath(xpath_search_bar)
# search_bar.click()  -> do not need to click on it
search_bar.send_keys('Selenium xpath')
sleep(2)
search_bar.submit()
sleep(2)

driver.close()
print("--- running %s seconds ---" % (time.time() - start_time))
