#!/usr/bin/env python
# encoding=utf-8

from bs4 import BeautifulSoup as bs
import requests as r
import csv
import re
import codecs
movies = []
url = ['https://movie.douban.com/top250?start={}'.format(str(i)) for i in range(0,226,25)]
for url in url[:]:
    html = r.get(url).text
    items = bs(html).find_all('div','item')
    for item in items:
        movie_name = item.find('span','title').string
        movie_rating = item.find('span','rating_num').string
        try:
            movie_quote = item.find('span','inq').string
        except:
            movie_quote='none'
        movie_info = item.find('div','bd').find('p','').get_text()
        movie_year = re.findall('\d{4}',movie_info)[0]
        movie_nation = re.findall('(?<=\d./).*(?=/)',movie_info)[0]
        movie = (movie_name,movie_year,movie_rating,movie_nation,movie_quote)
        #print(str(movie))
        movies.append(movie)

with codecs.open('DoubanMovieTOP250.csv','w','utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["电影名称","上映年份","评分","地区","简介"])
    writer.writerows(movies)