
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser=webdriver.Chrome()
browser.get('https://gmail.com/')
email=browser.find_element_by_name('identifier')
email.send_keys('enter your gmail address') #enter your email
emailsub=browser.find_element_by_id('identifierNext')
emailsub.click()


password=WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.NAME,'password')))

password.send_keys("enter your password")  #enter your password
passsub=browser.find_element_by_id('passwordNext')
passsub.click()









