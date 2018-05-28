from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from time import sleep
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
import os
import time


#set up driver, make chrome_path equal to location of your chromedriver.exe
chrome_path = r"C:\Users\*YOUR*\Python\chromedriver_win32\chromedriver.exe"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_path)
#the site which has the long scrolling page
driver.get("https://")

#if a button is blocking it from being done automatically, find its name and put it in **here**. For example instagram uses "Load more".
elm = driver.find_element_by_link_text('**here**')
driver.implicitly_wait(5)
elm.click()

lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
                lastCount = lenOfPage
                time.sleep(10)
                lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if lastCount==lenOfPage:
                    match=True
