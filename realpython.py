from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


class Scraper:
    def __init__(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def open(self, address):
        self.browser.get(address)

    def getUserPass(self, fileName):
        file = open(fileName, "r")
        content = file.read()
        file.close()
        self.username = content.split('user=', 1)[1].split('pass=', 1)[0].strip()
        self.password = content.split('pass=', 1)[1].strip()

    def login(self):
        username_box = self.browser.find_element(By.CSS_SELECTOR, "input[name='username']")
        password_box = self.browser.find_element(By.CSS_SELECTOR, "input[name='password']")
        username_box.send_keys(self.username)
        password_box.send_keys(self.password)
        login_btn = self.browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_btn.click()
        save_btn = self.browser.find_element(By.XPATH, "//button[text()='Save Info']")
        save_btn.click()
        sleep(2)
        notNow_btn = self.browser.find_element(By.XPATH, "//button[text()='Not Now']")
        notNow_btn.click()

    def closeBrowser(self):
        self.browser.close()

    def searchFor(self, keyword):
        searchBox = self.browser.find_element(By.XPATH, "//input[@placeholder='Search' and @type='text']")
        searchBox.send_keys(keyword)
        searchBox.send_keys(Keys.ENTER)

    def extractElements(self, fileName):
        file = open(fileName, "r")
        content = file.read()
        file.close()
        data = []
        while True:
            try:
                element = content.split('\n', 1)[0].strip()
                content = content.split('\n', 1)[1].strip()
                data.append(element)
            except:
                element = content
                data.append(element)
                break
        self.accounts = pd.DataFrame(data, columns=['name'])
        print(self.accounts)


if __name__ == "__main__":
    insta = Scraper()
    insta.open('https://instagram.com/')
    insta.getUserPass('pass.txt')
    insta.login()
    sleep(3)
    insta.searchFor('پسته')
    insta.extractElements('accounts.txt')
    insta.extractElements('tags.txt')
    sleep(6)
    insta.closeBrowser()
