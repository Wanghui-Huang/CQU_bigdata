# -*- coding: utf-8 -*-
import requests
import json

def nlp_demo():
    url = 'https://nlp-ext.cn-north-4.myhuaweicloud.com/v1/0e9ef150ac80f2be2ffcc01e74c6e26a/nlp-fundamental/ner'  # endpoint和project_id需替换
    #token请按照文档内容查询
    token = ''
    header = {
        'Content-Type': 'application/json',
        'X-Auth-Token': token
    }
    body = {
        'text': '《最佳拍档之女皇密令》是由新艺城出品的《最佳拍档》系列的第三部，由徐克担任执导，许冠杰，麦嘉，张艾嘉主演的一部喜剧片',
        'lang': 'zh'
    }
    resp = requests.post(url, data=json.dumps(body), headers=header)
    print(resp.text.encode('utf-8').decode("unicode_escape"))

if __name__ == '__main__':
    nlp_demo()
