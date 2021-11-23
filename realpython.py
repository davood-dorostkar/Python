from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('https://instagram.com/')
sleep(5)

passFile = open('pass.txt', "r")
content = passFile.read()
passFile.close()
username = content.split('user=', 1)[1].split('pass=', 1)[0].strip()
password = content.split('pass=', 1)[1].strip()

username_box = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
password_box = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
username_box.send_keys(username)
password_box.send_keys(password)
login_btn = browser.find_element(By.XPATH, "//button[@type='submit']")
login_btn.click()
sleep(5)
save_btn = browser.find_element(By.XPATH, "//button[text()='Save Info']")
save_btn.click()
sleep(2)
notNow_btn = browser.find_element(By.XPATH, "//button[text()='Not Now']")
notNow_btn.click()
sleep(5)
browser.close()
