#!/usr/bin/env python3
# coding: utf-8

import time
from selenium import webdriver
from selenium.webdriver import Chrome
from lxml import etree
from concurrent.futures import ThreadPoolExecutor, wait
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

laogou_url = "https://lagou.com"


def parse_lagou_html(html_text) -> zip:
    etree_html = etree.HTML(html_text)
    # position_id = etree_html.xpath(
    #     '//*[@id="s_position_list"]/ul/li[@class="con_list_item default_list"]/@data-positionid'
    # )
    position_name_list = etree_html.xpath(
        '//*[@id="s_position_list"]/ul/li[@class="con_list_item default_list"]/@data-positionname'
    )
    position_salary_list = etree_html.xpath(
        '//*[@id="s_position_list"]/ul/li[@class="con_list_item default_list"]/@data-salary'
    )

    return zip(position_name_list, position_salary_list)


def lagou_spider(city, job_dict):

    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("headless")
    web_browser = Chrome()

    job_set = set()
    web_browser.get(laogou_url)

    # 进入拉钩城市站
    time.sleep(2)
    web_browser.find_element_by_xpath(f'//a[@data-city="{city}"]').click()

    # 展开技术类职业选项
    time.sleep(1)
    web_browser.find_element_by_xpath('//*[@id="sidebar"]/div/div[1]/div[1]/div/i').click()

    # 进入 Python 相关职位页面
    time.sleep(1)
    web_browser.find_element_by_xpath(
        '//*[@id="sidebar"]/div/div[1]/div[2]/dl[1]/dd/a[12]/h3'
    ).click()

    page_num = 1
    job_num = 0
    while job_num < 100 or page_num > 10:
        page_num += 1
        time.sleep(2)
        scroll_js = '''window.scrollBy({
                  top: 5000,
                  behavior: 'smooth'
                })'''
        web_browser.execute_script(scroll_js)
        time.sleep(2)
        parse_result = parse_lagou_html(web_browser.page_source)
        job_set = job_set | set(parse_result)
        job_num = len(job_set)
        logger.debug(job_set)
        logger.info(f"already get job amount {job_num}")
        # 进入下一页
        try:
            web_browser.find_element_by_xpath(
                '//*[@id="order"]/li/div[4]/a[@class="next "]'
            ).click()
        except Exception as e:
            logger.error(e)
            break

    web_browser.close()

    job_list = list(job_set)[0:100]
    job_dict[city] = job_list


def main():
    job_dict = {}
    city_list = ["北京", "上海", "广州", "深圳"]
    with ThreadPoolExecutor(max_workers=4) as executor:
        all_task = [executor.submit(lagou_spider, city, job_dict) for city in city_list]
        wait(all_task, timeout=3600, return_when="ALL_COMPLETED")

    logger.info(f"job_dict: {job_dict}")


if __name__ == '__main__':
    main()
