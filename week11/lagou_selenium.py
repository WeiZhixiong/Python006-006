#!/usr/bin/env python3
# coding: utf-8

import time
from selenium import webdriver
from selenium.webdriver import Chrome
from lxml import etree
import pymysql
from concurrent.futures import ThreadPoolExecutor, wait
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

lagou_url = "https://lagou.com"
mysql_host = "my-host"
mysql_port = 3306
mysql_user = "test_user"
mysql_password = "********"
mysql_db = "lagou"
job_table = "job"


def parse_lagou_html(html_text) -> zip:
    """
    分析拉勾职位列表页面, 返回 (position_name_list, position_salary_list) 组成的可迭代对象
    :param html_text:
    :return:
    """
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
    web_browser.get(lagou_url)

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


def write_job_to_mysql(job_info_list):

    pymysql_conn = pymysql.connect(
        user=mysql_user,
        password=mysql_password,
        host=mysql_host,
        database=mysql_db,
        port=mysql_port
    )

    create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS `{job_table}` (
           `city` VARCHAR(100) NOT NULL,
           `job_name` VARCHAR(100) NOT NULL,
           `salary` VARCHAR(100) NOT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;    
    """

    insert_job_sql = f"insert into {job_table} (city, job_name, salary) values (%s, %s, %s)"

    with pymysql_conn:
        with pymysql_conn.cursor() as cursor:
            cursor.execute(create_table_sql)
            result = cursor.executemany(insert_job_sql, job_info_list)
            logger.info(f"insert job count {result}")
        pymysql_conn.commit()


def main():
    job_dict = {}
    city_list = ["北京", "上海", "广州", "深圳"]
    with ThreadPoolExecutor(max_workers=4) as executor:
        all_task = [executor.submit(lagou_spider, city, job_dict) for city in city_list]
        wait(all_task, timeout=3600, return_when="ALL_COMPLETED")

    logger.info(f"job_dict: {job_dict}")

    job_info_list = []
    for city, job_list in job_dict.items():
        for job_info in job_list:
            if job_info:
                job_info_list.append((city, job_info[0], job_info[1]))

    if job_info_list:
        write_job_to_mysql(job_info_list)


if __name__ == '__main__':
    main()
