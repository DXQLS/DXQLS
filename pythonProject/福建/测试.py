import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

# 设置允许跨域
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Content-Type': '*'
}

data = {
    "cis_req_params": "11b104412bf3647882aaca9b921068cdc0908375892757f3d1dcf1370a5b08dd99b1da840bcb0878a54d9c9cbd4ca72e3a1ac876090cae8e79bd33afac5b7d0d73ec046c2c80153c7cb288307b4b2a88",
    "cis_fingerprint": "c311c8b89cfe398e446c34053dec70b1808eb407802ffc3a92f47eda29be466d"
}
url = 'https://ggfw.ybj.ln.gov.cn/hsa-pss-pw/web/pw/terms/queryWmBypage'

res = requests.post(url=url,json= data ,headers=headers )

print(res.json())