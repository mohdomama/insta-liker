from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os, time 
import getpass,sys


def setup():
   
    global browser
    driverPath = os.getcwd()+'/chromedriver'
    url = r'https://www.instagram.com/accounts/login/'
    chromeOptions = webdriver.ChromeOptions()
    #chromeOptions.binary_location='/opt/google/chrome/google-chrome'

    '''                                             #These arguments make chrome run headless.Unfortunately the chrome headless is in beta and hence considerably slow.
    chromeOptions.add_argument("--headless")            
    chromeOptions.add_argument("--disable-gpu")
    chromeOptions.add_argument("--start-fullscreen")
    '''

    prefs = {"profile.managed_default_content_settings.images":2}
    chromeOptions.add_experimental_option("prefs",prefs)
    print('reached 1')
    browser = webdriver.Chrome(driverPath,chrome_options=chromeOptions)
    print('reached')
    #browser.set_window_position(-10000000, 0)       #move chrome away from view
    print('Fetching login page..')
    browser.get(url)
    print('reached login page')    

def login(username,password):
    print('logging in..')
    element = browser.find_element_by_name('username')
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
            break
        elif time.time()-loginTime>10:                  #if login takes more than 10 seconds, tell user that his internet is slow
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
                #do nothing
                pass

    print('login complete')

def scroll(number_posts):
    scroll_xpath=r"//span[text()='Like' or text()='Unlike']"
    print('Scrolling..')

    while True:
        try:
            try:
                posts=len(browser.find_elements_by_xpath(scroll_xpath))
            except:
                posts = 0
            
            print(posts)

            if(posts>=int(number_posts)):
                break
            else:
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        except Exception as e:
            print("Reached Exceptio\n",e)
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            



def like(number_posts):
    likeNumber=0
    print('Liking the posts..')
    elements = browser.find_elements_by_xpath(r"//span[text()='Like' or text()='Unlike']")
    for i in range (int(number_posts)):
        if elements[i].text=='Like':
            print('Liked')
            likeNumber+=1
            try:
                elements[i].click()
            except:
                print('some excetion for ',i)

    
    print('Liking Finished!!\n{} posts liked!'.format(likeNumber))

def main():
    
    username = input('Enter your instagram username:\n')
    password = getpass.getpass('Enter your instagram password:\n')
    number_posts = input('Enter the numer of posts you wish to like:\n')
    start_time = time.time()
    setup()
    login(username,password)
    scroll(number_posts)
    like(number_posts)
    print('Time taken = ',time.time()-start_time)
    browser.close()


if __name__=='__main__':
    main()
