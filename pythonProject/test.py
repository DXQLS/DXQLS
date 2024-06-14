import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import time
# 设置允许跨域
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Content-Type': '*',
    'Cookie':'headerStatus=-1; headerShow=true; SESSION_FLAG=0; EXIT_STAMP=1715927556711'
}



# url = 'https://ybj.qinghai.gov.cn/qhggfw/hsa-rest-ba-plaf/core/app/queryMedisInfo'
# ajsx = requests.post(url=url,json=data,timeout=10)
# data = ajsx.json()
# print(data['data']['list'])

for i in range(1,3):
    data = {
        "pageSize": 10,
        "pageNum": i,
        "list_type": "101",
        "hilist_name": "",
        "insu_admdvs": "",
        "hilist_code": ""
    }
    data_list = []
    url = 'https://ybj.qinghai.gov.cn/qhggfw/hsa-rest-ba-plaf/core/app/queryMedisInfo'
    ajsx = requests.post(url=url, json=data, timeout=10)
    data = ajsx.json()
    data = data['data']['list']
    data_list.extend(data)

print(data_list)