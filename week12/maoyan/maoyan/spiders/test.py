
# coding: utf-8

from lxml import etree

with open('./maoyan_movie.html', 'rb') as f:
    html_str = f.read().decode()

html_etree = etree.HTML(html_str)
movie_name_list = html_etree.xpath('//div[@class="movie-hover-info"]/div[@class="movie-hover-title"]/span[@class="name "]/text()')
movie_type_list = html_etree.xpath('//a/div[@class="movie-hover-info"]/div[@class="movie-hover-title"][2]/text()')
movie_type_list = movie_type_list[::-2]
movie_type_list.reverse()
movie_show_time = html_etree.xpath('//a/div[@class="movie-hover-info"]/div[@class="movie-hover-title movie-hover-brief"]/text()')
movie_show_time = movie_show_time[::-2]
movie_show_time.reverse()

# html = """<div class="movie-hover-title" title="人潮汹涌" >
#               <span class="hover-tag">类型:</span>
#               剧情／喜剧／爱情
#             </div>"""
#
# html_etree = etree.HTML(html)
#
# movie_type_list = html_etree.xpath('//div[@class="movie-hover-title"]/text()')
# print(movie_type_list)