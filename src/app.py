from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import shutil
from xlsxwriter import Workbook
import credentials as c
# from credentials import instagram_user_name, instagram_password
# from time import sleep
import os
import time
start_time = time.time()


#  This class is for testing purposes only. It is wrong on many levels.
class App:
    def __init__(self, username=c.instagram_user_name, password=c.instagram_password,
                 target_username='fruskac', path='C:\est\photos'):
        self.username = username
        self.password = password
        self.target_username = target_username
        self.path = path
        self.driver = webdriver.Chrome('C:\est\chromedriver_win32\chromedriver.exe')
        self.error = False
        self.main_url = 'https://www.instagram.com'
        self.driver.get(self.main_url)
        time.sleep(2)
        #  login into instagram
        self.log_in()
        if self.error is False:
            #  open target profile
            self.close_turn_on_notifications()
            self.open_target_profile()

        #  This code flow is insane, I doubt that this is a good practice
        if self.error is False:
            #  find targets number of posts
            self.scroll_down()
        #  If path does not exist, create one
        if self.error is False:
            if not os.path.exists(path):
                os.mkdir(path)

        if self.error is False:
            self.downloading_images()

        time.sleep(3)
        self.driver.close()

     #  @staticmethod  # this warning annoyed me, so i put @staticmethod
    def write_captions_to_excel_file(self, images, caption_path):
        print('Writing to excel.')
        workbook = Workbook(os.path.join(caption_path, 'captions.xlsx'))
        worksheet = workbook.add_worksheet()
        row = 0
        worksheet.write(row, 0, 'Image name')  # 3 args -> row num, column num, value
        worksheet.write(row, 1, 'Caption')
        row += 1
        for i, image in enumerate(images):
            #  repeating -> candidate for naming function
            file_name = 'image_' + str(i) + '.jpg'
            try:
                caption = image['alt']
            except KeyError:
                caption = 'No caption exists'
                print('File ', file_name, ' does not have caption!')
            worksheet.write(row, 0, file_name)
            worksheet.write(row, 1, caption)
            i += 1
            row += 1
        workbook.close()  # Always close excel file, or any file...

    def download_captions(self, images):
        captions_folder_path = str(os.path.join(self.path, 'captions'))
        if not os.path.exists(captions_folder_path):
            os.mkdir(captions_folder_path)
        self.write_captions_to_excel_file(images, captions_folder_path)

        '''for i, image in enumerate(images):
            try:
                caption = image['alt']
            except KeyError:
                caption = 'No caption exists for this image'
            file_name = 'caption' + str(i) + '.txt'
            file_path = os.path.join(captions_folder_path, file_name)
            link = image['src']
            with open(file_path, 'wb') as file:
                file.write(str('link:'+str(link)+'\n'+'caption:'+caption).encode())'''

    def downloading_images(self):
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        all_images = soup.find_all('img')
        print('Number of images: ', len(all_images))
        self.download_captions(all_images)
        for i, image in enumerate(all_images):
            filename = 'image_' + str(i) + '.jpg'
            # image_path = self.path + '/' + filename
            image_path = os.path.join(self.path, filename)
            link = image['src']
            print('Downloading image ', i)
            response = requests.get(link, stream=True)
            try:
                with open(image_path, 'wb') as file:
                    shutil.copyfileobj(response.raw, file)
            except Exception as e:
                print(e)
                print('Could not download image number ', i)
                print('Image link --> ', link)

    def scroll_down(self):
        try:
            x_number_of_posts = '//span[@class="g47SY "]'
            number_of_posts = self.driver.find_element_by_xpath(x_number_of_posts)
            time.sleep(1)
            # if there are 15,300 posts -> 15300
            #  I am defining self.attribute outside of __init__???
            self.num_of_posts = int(str(number_of_posts.text).replace(',', ''))
            if self.num_of_posts > 12:
                num_of_scrolls = int((self.num_of_posts/12) + 3)
                # +3 is for any case
                try:
                    print('How many times it needs to scroll down:')
                    for value in range(num_of_scrolls):
                        print(value)
                        #  Doing some JS for scrolling down
                        js_scroll = 'window.scrollTo(0, document.body.scrollHeight);'
                        self.driver.execute_script(js_scroll)
                        time.sleep(1)
                except Exception as e:
                    self.error = True
                    print(e)
                    print('Error occurred while trying to scroll down')

        except Exception:
            self.error = True
            print('Could not find num of posts while trying to scroll down')

    def open_target_profile(self):
        try:
            time.sleep(1)
            self.driver.get(self.main_url + '/' + self.target_username + '/')
            time.sleep(1)
        except Exception:
            self.error = True
            print('Could not open target profile')

    def close_turn_on_notifications(self):
        try:
            time.sleep(1)
            xpath_close_n = '//button[@class="aOOlW   HoLwm "]'
            close_notifications = self.driver.find_element_by_xpath(xpath_close_n)
            close_notifications.click()
            time.sleep(1)

        except Exception:
            pass

    def log_in(self):
        try:
            log_in_path = '//p[@class="izU2O"]/a'
            log_in_button = self.driver.find_element_by_xpath(log_in_path)
            log_in_button.click()
            time.sleep(2)  # It does not work without sleep here, retarded like ahk
            try:
                x_user_name_input = '//input[@name="username"]'
                #  Variants for xpath_user_name_input:
                # '//form[@class="HmktE"]//input[@username="username"]'
                # '//input[@aria-label="Phone number, username, or email"]'
                # user_name_input = self.driver.find_element_by_link_text('Sign up')
                user_name_input = self.driver.find_element_by_xpath(x_user_name_input)
                user_name_input.send_keys(self.username)

                x_user_pass_input = '//input[@name="password"]'
                user_password_input = self.driver.find_element_by_xpath(x_user_pass_input)
                user_password_input.send_keys(self.password)
                user_password_input.submit()
            except Exception:
                print("Exception occurred while trying to find username or pass field!")
                self.error = True

        except Exception:
            #  Too broad Exception
            self.error = True
            print('Unable to find log in button')


if __name__ == '__main__':
    app = App(target_username='pi1mg')

#  Running time:
print('Runnung time is: {} seconds'.format(round(time.time()-start_time, 2)))

'''
Best practices:
1- Avoid using Selenium
2- Limit requests to the server
3- Download web pages
4- Parse pessimistically (bzw. convert num to str for any case)
5- Divide and conquer
'''