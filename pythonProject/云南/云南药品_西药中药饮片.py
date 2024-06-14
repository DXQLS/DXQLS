import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 设置允许跨域的请求头
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Content-Type': '*'
}

# 设置请求重试策略
retry_strategy = Retry(
    total=3,  # 重试总次数
    backoff_factor=1,  # 重试间隔时间的增长因子
    status_forcelist=[429, 500, 502, 503, 504],  # 需要重试的状态码
    method_whitelist=["HEAD", "GET", "OPTIONS", "POST"]  # 需要重试的方法
)

adapter = HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)

all_data = []

for i in range(1, 13656):
    data = {
        "pageNum": i,
        "pageSize": 10,
        "listType": 102,
        "usedCache": False,
        "medListCodg": "",
        "regName": "",
        "drugGenname": "",
        "hilistCode": ""
    }
    url = 'https://ggfw.ynylbz.cn/hsa-pss-pw/web/pw/polcent/queryHilist'
    try:
        result = http.post(url=url, json=data, headers=headers, timeout=10)
        result.raise_for_status()
        result_json = result.json()
        datas = result_json['data']['list']
        all_data.extend(datas)
        print(f'正在爬取第{i}页的数据，共计爬取{len(all_data)}条数据')
    except requests.exceptions.RequestException as e:
        print(f'第{i}页请求失败，错误：{e}')
    except KeyError as e:
        print(f'解析数据时发生错误：{e}')
    except Exception as e:
        print(f'其他错误：{e}')

if all_data:
    df = pd.DataFrame(all_data)
    df_filtered = df[
        ['hilistCode',
         'hilistName',
         'chrgitmLv',
         'stdName'
         ]
    ]
    df_filtered.columns = [
        '医疗目录编码',
        '中药饮片名称',
        '医保支付类别',
        '标准名称'
    ]
    df_filtered.to_excel('D:\pythonProject\pythonProject\云南\云南药品_西药中药饮片.xlsx', index=False)
    print(f'数据已写入表格，共计{len(df_filtered)}条数据')
else:
    print('没有获取到任何数据')
