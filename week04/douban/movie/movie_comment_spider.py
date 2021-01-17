#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import sys
from lxml import etree
import logging
import time
import requests

# 改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

movie_id = "24298954"
comment_url_template = "https://movie.douban.com/subject/%s/comments?start=%s&limit=%s&status=P&sort=new_score"
req_headers = {
    "accept-language": "en",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
}
comment_record_file = f"{movie_id}.csv"


def parse_comment_html(html_str):
    result = []
    page_dom = etree.HTML(html_str)
    comment_dom_list = page_dom.xpath("/html/body/div[3]/div[1]/div/div[1]/div[4]/div[*]")
    for comment_dom in comment_dom_list:
        try:
            comment_time = comment_dom.xpath("div[2]/h3/span[2]/span[3]//@title")[0]
            comment_content = comment_dom.xpath("div[2]/p/span//text()")[0]
            comment_star = comment_dom.xpath("div[2]/h3/span[2]/span[2]//@class")[0]
            comment_star = int(int(comment_star.split("allstar")[1].split(" rating")[0]) / 10)
        except Exception as e:
            logger.error(e)
            continue
        result.append(f"{comment_time},{comment_star},{repr(comment_content)}\n")
    return result


def main():
    comment_start = 0
    step = 20
    comment_stop = 40
    while comment_stop > comment_start:
        comment_url = comment_url_template % (movie_id, comment_start, step)
        comment_start += step
        time.sleep(3)
        comment_req = requests.get(comment_url, headers=req_headers)
        page_str = comment_req.content.decode("utf-8")
        comment_list = parse_comment_html(page_str)
        with open(comment_record_file, "a") as f:
            f.writelines(comment_list)


if __name__ == "__main__":
    main()
