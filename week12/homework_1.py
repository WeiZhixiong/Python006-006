#!/usr/bin/env python3
# coding: utf-8

import requests
from bs4 import BeautifulSoup

maoyao_url = "https://maoyan.com/films?showType=3"
movie_list_file = "movie_list.csv"


def main(request_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "no-cache",
        "Cookie": "your cookie"
    }

    req = requests.get(request_url, headers=headers)
    page_content = req.content.decode()
    soup = BeautifulSoup(page_content, 'html.parser')
    movies_dict = {}

    for tags in soup.find_all('div', attrs={'class': 'movie-hover-info'}):
        movie_name = tags.find('span', attrs={'class': 'name'}).string
        movies_dict[movie_name] = {}
        movie_attr = tags.find_all('div', attrs={'class': 'movie-hover-title', 'title': movie_name})
        for i in movie_attr:
            attr = i.span.string
            value = i.contents[2].strip()
            movies_dict[movie_name][attr] = value

    write_lines = []

    for movie_name, movie_attr in movies_dict.items():
        movie_type = movies_dict[movie_name]["类型:"]
        show_time = movies_dict[movie_name]["上映时间:"]
        write_lines.append(f"{movie_name},{movie_type},{show_time}\n")

    with open(movie_list_file, 'w') as f:
        f.writelines(write_lines[:10])


if __name__ == '__main__':
    main(maoyao_url)
