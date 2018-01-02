from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

import os, time 
import getpass,sys


def setup():
    global browser
    PATH = os.environ['PATH']
    pwd = os.getcwd()
    os.environ['PATH'] = PATH + ':' + pwd

    url = r'https://www.instagram.com/accounts/login/'

    firefoxProfile = FirefoxProfile()
    firefoxProfile.set_preference('permissions.default.stylesheet', 2)
    firefoxProfile.set_preference('permissions.default.image', 2)
    firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so',
                                  'false') 

    browser = webdriver.Firefox(firefoxProfile)
    #browser.set_window_position(-10000000, 0)       #move chrome away from view
    print('Fetching login page..')
    browser.get(url)
    print('reached login page')   


def login(username,password):
    print('logging in..')
    while True :
        try:
            element = browser.find_element_by_name('username')
            break
        except:
            pass
    element.clear()
    element.send_keys(username)

    element = browser.find_element_by_name('password')
    element.clear()
    element.send_keys(password)

    element.send_keys(Keys.RETURN)

    #check if the username and password are correct
    loginTime=time.time()
    while True:
        if browser.current_url=='https://www.instagram.com/':
            time.sleep(2)
            break

        #if login takes more than 10 seconds, tell user that his internet is slow
        elif time.time()-loginTime>10:                 
                print('Your Internet seems slow!\n',e)
                browser.close()
                sys.exit()
        else:
            try:
                element=browser.find_element_by_xpath("//*[@id='slfErrorAlert']")
                print('\n'+element.text)
                print('Enter your credentials again!\n')
                browser.close()
                main()
                sys.exit()
            except:
                pass

    print('login complete')
            

def scroll_and_like(number_posts):
    scroll_xpath=r"//span[text()='Like']"
    print('Scrolling..')
    count = 0
    while (count < int(number_posts)):
        try :
            element = browser.find_element_by_xpath(scroll_xpath)
            element.click()
            count+=1
            print ('Liked! Like count :', count)
        except Exception as e:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        

def main():
    
    keys = open('keys.txt',mode='rt')
    username = keys.readline().strip()
    password = keys.readline().strip()
    number_posts = input('Enter the numer of posts you wish to like:\n')
    start_time = time.time()
    setup()
    login(username,password)
    scroll_and_like(number_posts)
    #like(number_posts)
    print('Time taken = ',time.time()-start_time)
    browser.close()


if __name__=='__main__':
    main()
