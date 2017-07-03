#!/usr/bin/python 
# -*- coding: utf-8 -*-  
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")

from selenium import webdriver
#import mouse operations 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

delay = 10 # seconds

questions = raw_input()
arr = questions.split('/')

#open the geekqanda.com
browser = webdriver.Firefox()
browser.get('http://www.geekqanda.com')

browser.find_element_by_id('qa-userid').send_keys('xxx@xxx.com')
browser.find_element_by_id('qa-password').send_keys('********')
browser.find_element_by_id('qa-login').send_keys(Keys.ENTER)

for item in arr:
    question = item
    try:
        WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div/div[1]/ul/li[7]/a")))
        print "catch a successful!"
        #enter the button by xpath
        browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/ul/li[7]/a").send_keys(Keys.ENTER)
        try:
            WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID,"title")))
            print "catcj title successful"
            browser.find_element_by_id('title').send_keys(unicode(question))
            Select(browser.find_element_by_id("category_1")).select_by_value("10")
            browser.find_element_by_id('tags').send_keys(unicode('其他'))
            browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[3]/div/form/table/tbody/tr[10]/td/label/input').click()
            browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[3]/div/form/table/tbody/tr[13]/td/input').send_keys(Keys.ENTER)
        except TimeoutException:
            print "catch title failed!"
    except  TimeoutException:
        print "catch a failed!"
