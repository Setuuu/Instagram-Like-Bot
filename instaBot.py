from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def wait():
    time.sleep(3)

#Class for the instagram bot
class instaBot:
    def __init__(self,username,password,hashtag):
        self.username = username
        self.password = password
        self.hashtag = hashtag
        self.web = webdriver.Firefox()
    def login(self):
        self.web.get("https://www.instagram.com/?hl=en")
        wait()
        username = self.web.find_element_by_name('username')
        password = self.web.find_element_by_name('password')
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
    #Function to handle the notification
    def notificationException(self):
        time.sleep(10)
        self.web.find_element_by_class_name("aOOlW.HoLwm").click()

    #Function to beging searching for the desired hashtag
    def searchHashtag(self):
        wait()
        search = self.web.find_element_by_class_name('XTCLo.x3qfX')
        search.send_keys(self.hashtag)
        wait()
        search.send_keys(Keys.ENTER)
        search.send_keys(Keys.ENTER)

    #Function that scrolls down the page a set number of times
    def scroll(self):
        wait()
        for i in range(5):
            self.web.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            wait()

    #Function that obtains the URLS of each post, and likes each one
    def likePost(self):
        post = []
        posts = self.web.find_elements_by_tag_name('a')
        for val in posts:
            #specify that posts get added to the list, rather than other links on the current page
            if "/p/" in val.get_attribute('href'):
                post.append(val.get_attribute('href'))
        for pic in post:
            self.web.get(pic)
            time.sleep(6)
            try:
                self.web.find_element_by_class_name("wpO6b ").click()
            except Exception as e:
                time.sleep(3)

#Creating the instance
instaBot = instaBot('YOUR-USERNAME','YOUR-PASSWORD','#YOUR-HASHTAG')
instaBot.login()
instaBot.notificationException()
instaBot.searchHashtag()
instaBot.scroll()
instaBot.likePost()