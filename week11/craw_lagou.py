#!/usr/bin/env python3
# coding: utf-8

import time
from selenium import webdriver

driver = webdriver.Chrome()

lagou_url = "https://www.lagou.com/"

city_list = ["北京", "上海", "广州", "深圳"]

driver.get(lagou_url)
time.sleep(3)
driver.find_element_by_xpath('//a[@data-city="上海"]').click()

time.sleep(3)
driver.find_element_by_xpath('//*[@id="sidebar"]/div/div[1]/div[1]/div/i').click()

time.sleep(1)
driver.find_element_by_xpath('//*[@id="sidebar"]/div/div[1]/div[2]/dl[1]/dd/a[12]/h3').click()

