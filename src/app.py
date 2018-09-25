from selenium import webdriver
import credentials
# from credentials import instagram_user_name, instagram_password
# from time import sleep
import time
start_time = time.time()


#  This class is for testing purposes only. It is wrong on many levels.
class App:
    def __init__(self, username=credentials.instagram_user_name,
                 password=credentials.instagram_password,
                 target_username='fruskac', path='C:\est\photos'):
        self.username = username
        self.password = password
        self.target_username = target_username
        self.path = path
        self.driver = webdriver.Chrome('C:\est\chromedriver_win32\chromedriver.exe')
        self.main_url = 'https://www.instagram.com'
        self.driver.get(self.main_url)
        time.sleep(3)
        #  write log in fuction
        self.log_in()

        time.sleep(3)
        self.driver.close()

    def log_in(self):
        log_in_path = '//p[@class="izU2O"]/a'
        log_in_button = self.driver.find_element_by_xpath(log_in_path)
        log_in_button.click()
        # input('Stop for now')


if __name__ == '__main__':
    app = App()

#  Running time:
print('Runnung time is: {} seconds'.format(round(time.time()-start_time)))
