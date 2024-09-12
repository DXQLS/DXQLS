import requests
import json


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://ggfw.ynylbz.cn",
    "Pragma": "no-cache",
    "Referer": "https://ggfw.ynylbz.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "Hm_lvt_2e9e12b673ad61053eabf1dbc33f8217": "1725954024,1726037691",
    "HMACCOUNT": "1E14B2327DDD5FAB",
    "SESSION_FLAG": "2",
    "Hm_lpvt_2e9e12b673ad61053eabf1dbc33f8217": "1726037731",
    "headerShow": "false"
}
url = "https://ggfw.ynylbz.cn/hsa-pss-pw/web/pw/polcent/queryHilist"
data = {
    "listType": "101",
    "hilistCode": "",
    "regName": "",
    "drugGenname": "",
    "valiFlag": 1,
    "pageNum": 1,
    "pageSize": 10,
    "usedCache": False
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.json())
print(response)
