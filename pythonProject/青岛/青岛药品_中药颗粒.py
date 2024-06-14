import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

# 设置允许跨域
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Content-Type': '*'
}
all_data = []


def is_server_up(url):
    try:
        requests.get(url, headers=headers, timeout=5)
        return True
    except requests.exceptions.RequestException as e:
        print(f"服务器检查失败： {e}")
        return False


def make_retrying_requests(max_retries):
    session = requests.Session()
    retries = Retry(total=max_retries,
                    backoff_factor=0.1,
                    status_forcelist=[500, 502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))
    session.mount('https://', HTTPAdapter(max_retries=retries))
    return session


# 创建具有重试功能的请求会话
session = make_retrying_requests(max_retries=5)

for i in range(1, 383):
    data_1 = {
        "pageNo": i,
        "pageSize": 50,
        "medListCodg": "",
        "listtype": 106
    }
    datas_2 = []
    url_1 = 'https://wbdt.ybj.qingdao.gov.cn/pss-gw/api/pss-pw/web/pw/pub/getHilistBDicList'
    if not is_server_up(url_1):
        print(f"服务器 {url_1} 当前不可用，跳过本次循环。")
        continue
    try:
        respones_1 = session.post(url=url_1, json=data_1, headers=headers, timeout=10).json()
        source_data = respones_1['data']  # 原始数据
        datas_1 = source_data['list']
        pages = data_1['pageNo']
        # print("**********"+str(datas_1))
        for data1 in datas_1:
            hilistCode = data1['hilistCode']
            # hilistCode = datas_1[0]['hilistCode'] if datas_1 else None
            # print('hilistCode' + hilistCode)
            if not hilistCode:
                print(f"没有获取到医疗目录编码，跳过本次循环。")
                continue
            data_2 = {
                "pageNo": 1,
                "pageSize": 20,
                "division": "",
                "medIns": "",
                "medListCodg": hilistCode
            }
            # print("data_2:" + str(data_2))
            url_2 = 'https://wbdt.ybj.qingdao.gov.cn/pss-gw/api/pss-pw/web/pw/getHilistSelfpay'
            # if not is_server_up(url_2):
            #     print(f"服务器 {url_2} 当前不可用，跳过本次循环。")
            #     continue

            respones_2 = session.post(url=url_2, json=data_2, headers=headers, timeout=10).json()
            # datas_2.append(respones_2['data']['list'])
            datas_2 = respones_2['data']['list']
            # print(datas_1, datas_2)
            # print(datas_2)
        for item1 in datas_1:
            for item2 in datas_2:
                new_data = {**item1, **item2}
                # print(new_data)
                all_data.append(new_data)
                print('正在爬取' + f'{pages}' + '页的数据，共计爬取' + f'{len(all_data)}' + '条数据')
    except requests.exceptions.RequestException as e:
        print(f"请求 {url_2} 失败： {e}")
        continue

df = pd.DataFrame(all_data)
df_filtered = df[
    ['hilistCode',
     'hilistName',
     'drugSpec',
     'specMol',
     'medChrgitmType',
     'chrgitmLv',
     'lstdFilNo',
     'begndate',
     'prodentpName',
     'selfpayProp',
     'selfpayPropPsnType'
     ]
    ]
df_filtered.columns = \
    ['医疗目录编码',
     '名称',
     '规格',
     '包装规格',
     '医疗收费项目类别',
     '收费项目等级',
     '上市备案号',
     '开始日期',
     '生产企业名称',
     '自付比例',
     '人员类别'
     ]
# print(df_filtered)
df_filtered.to_excel('D:\pythonProject\pythonProject\青岛\青岛药品_中药颗粒集采.xlsx', index=False)
print('数据已写入表格，共计' + format(len(df)))