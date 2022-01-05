# -*- coding: utf-8 -*-
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe')


def get_one_detail(name):
    url = 'https://baike.baidu.com/item/'+name
    driver.get(url)
    # time.sleep(1)

    desc = driver.find_element_by_class_name('lemma-summary').text.split('。')[0]

    return desc


names = []
with open("movies.txt", 'r') as f:
    names = f.read().splitlines()


for i in names[1800:2000]:
    try:
        one_people_list = get_one_detail(i)
        print(one_people_list)
        if '《' in one_people_list:
            with open("des_tp.txt", 'a') as f:
                    f.write(one_people_list+'\n')
    except:
        continue

