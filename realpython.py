from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class Scraper:
    def __init__(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def open(self, address):
        self.browser.get(address)

    def getUserPass(self, fileName):
        passFile = open(fileName, "r")
        content = passFile.read()
        passFile.close()
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


if __name__ == "__main__":
    insta = Scraper()
    insta.open('https://instagram.com/')
    insta.getUserPass('pass.txt')
    insta.login()
    sleep(3)
    insta.closeBrowser()
