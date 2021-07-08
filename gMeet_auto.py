import time
import schedule
from selenium import webdriver
import selenium
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement



drivers = webdriver.Firefox()
drivers.get('https://google.com')
time.sleep(2)

signin = drivers.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div[2]/a').click()
time.sleep(2)

emailid = '' #add
password = '' #add
username = drivers.find_element_by_xpath('//*[@id="identifierId"]').send_keys(emailid)
time.sleep(2)

nxt = drivers.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()


#anyone knows how to bypass google login restrications 