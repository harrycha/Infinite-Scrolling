from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from time import sleep
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
import os
import time


#set up driver, the r is rob which has to be done
chrome_path = r"C:\Users\harry\Python\chromedriver_win32\chromedriver.exe"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_path)
#get site
driver.get("https://")

#if there is a think you need to click first eg link
elm = driver.find_element_by_link_text('Load more')
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