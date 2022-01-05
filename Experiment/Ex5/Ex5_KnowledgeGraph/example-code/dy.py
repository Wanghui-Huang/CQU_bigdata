"""
-*- coding: utf-8 -*-
@Time : 2021/11/6 下午 4:59
@Author : SunGuoqi
@Website : https://sunguoqi.com
@Github: https://github.com/sun0225SUN
"""

# 导入一些模块
import requests
import re
import time
from bs4 import BeautifulSoup

def once(page):
    url = 'http://dianying.im/pianku-dianying--------'
    url += str(page) + '---/'
    # UA伪装
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    # 发起请求
    response = requests.get(url, headers=headers)
    # 获得响应文件文本
    # print(response.text)
    html = response.text
    # 创建BeautifulSoup对象，方便解析
    soup = BeautifulSoup(html, 'lxml')
    # 找出所有的li标签
    all_li = soup.find('div', {'class': 'module-items'}).find_all('div', {'class': 'module-item-cover'})
    # 创建一个空列表，存放我们的数据。
    # print(all_li)
    for item in all_li:
        # 提取影片名称
        name = item.find('a')['title']
        # 把数据按找字典的格式存放到列表里
        print(name, file=open("movies2.txt", "a"))


for i in range(50):
    print(i)
    once(i)
    time.sleep(1)
