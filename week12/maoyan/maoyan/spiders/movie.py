import scrapy
from scrapy.selector import Selector
from ..items import MaoYanItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Cache-Control": "no-cache",
        }

        cookies = {
            "uuid_n_v": "v1",
        }

        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=headers, cookies=cookies)

    def parse(self, response):
        html_etree = Selector(response=response)
        movie_name_list = html_etree.xpath(
            '//div[@class="movie-hover-info"]/div[@class="movie-hover-title"]/span[@class="name "]/text()').getall()
        movie_name_list = movie_name_list[:10]
        movie_type_list = html_etree.xpath(
            '//a/div[@class="movie-hover-info"]/div[@class="movie-hover-title"][2]/text()').getall()
        movie_type_list = movie_type_list[::-2]
        movie_type_list.reverse()
        movie_show_time = html_etree.xpath(
            '//a/div[@class="movie-hover-info"]/div[@class="movie-hover-title movie-hover-brief"]/text()').getall()
        movie_show_time = movie_show_time[::-2]
        movie_show_time.reverse()
        movie_info_list = zip(movie_name_list, movie_type_list, movie_show_time)
        for movie_info in movie_info_list:
            item = MaoYanItem()
            item["movie_name"] = movie_info[0]
            item["movie_type"] = movie_info[1].lstrip().strip()
            item["show_time"] = movie_info[2].lstrip().strip()
            yield item
