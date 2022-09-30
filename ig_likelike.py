from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from selenium.common.exceptions import NoSuchElementException


chromedriver_path = r'./chromedriver' 
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(1)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)

# commentsDict = [ "nice","good","beautiful","awesome","amazing","fab","mindblowing"]

username = webdriver.find_element_by_name('username')
username.send_keys('enter username here')
password = webdriver.find_element_by_name('password')
password.send_keys('enter password herel')
button_login = webdriver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button > div')
button_login.click()
sleep(8)

try:
    notsave = webdriver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
    notsave.click()
    sleep(5)
except:    
    sleep(2)

try:
    notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
    notnow.click() 
    sleep(3)
except:    
    sleep(2)

sleep(1)
usernameofperson="hsiuchi_1215" # enter the other username whose post you want to like and comment
webdriver.get('https://www.instagram.com/' + usernameofperson)
sleep(5)
first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]')
first_thumbnail.click()
sleep(5)
next_post='1'
null=''
liked,unlike=0,0
while next_post is not null:
    if liked>0 or unlike>0:
        next_post.click()
        sleep(7)
    like = webdriver.find_element_by_xpath("//*[@aria-label='Like']")
    like.click()
    liked +=1
    sleep(5)
    # commentArea = webdriver.find_element_by_class_name('Ypffh')
    # commentArea.click()
    sleep(1)
    # commentArea = webdriver.find_element_by_class_name('Ypffh')
    # commentArea.send_keys(random.choice (commentsDict))
    sleep(1)
    # commentArea.send_keys(Keys.ENTER)
    sleep(5)               
    try:
        next_post = webdriver.find_element_by_link_text('Next')
    except :
        next_post = null
    if liked%10==0:
        print(liked)
print(str(liked)+' Posts Liked!')