import json
import pandas as pd
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
}

url = "https://jyapi.gdmede.com.cn:446/public/priceInfoPublicPage/index"

params = {
    "pageNum": 1,
    "pageSize": 150,
    "showSearch": '',
    "searchValue": '',
    "prodType": '',
    "prodId": '',
    "yPid": '',
    "nameCn": '',
    "price": '',
    "spec": '',
    "smlName": '',
    "warpName": '',
    "facName": '',
    "attrName": '',
    "convert": '',
    "prodTrade": '',
    "wh": '',
    "priceUnit": '',
    "nhiGroupCode": '',
    "convertPer": '',
    "convertSpec": '',
    "convertUnit": '',
    "ybType": '',
    "qualityEvaluation": '',
    "jgAttCou": '',
    "type": '',
    "sourceStr": '',
    "briskFlag": ''
}

# 初始化data_list
data_list = []

# 循环直到最大页码数
for pageNum in range(1, 388):
    params["pageNum"] = pageNum
    response = requests.get(url, params=params, headers=headers)
    content = response.content.decode()

    # 搜索包含数据列表的JSON字符串
    data_list_pattern = r"dataList:\s*\[(.*?)\]"
    data_list_match = re.search(data_list_pattern, content)

    if data_list_match:
        data_list_str = data_list_match.group(1)
        # 将当前页的数据添加到data_list中
        data_list.extend(json.loads(f'[{data_list_str}]'))
        print('当前正在爬取第'+ f'{pageNum}' + '页，共爬取'+ f'{len(data_list)}' + '数据')
    else:
        print(f"没有找到dataList, pageNum: {pageNum}")
        break

# 将data_list转换为DataFrame
df = pd.DataFrame(data_list)
df_filtered = df[
        ['prodId',
         'nameCn',
         'spec',
         'smlName',
         'convert',
         'facName',
         'price',
         'priceUnit',
         'pid',
         'warpName',
         'nhiGroupCode',
         'wh',
         'priceUnit',
         'ybType',
         'jgAttCou',
         'type'
         ]
]

df_filtered.columns = \
    ['产品编码',
     '产品名称',
     '规格',
     '剂型',
     '包装',
     '生产企业',
     '价格',
     '包装价格',
     '药交ID',
     '包材',
     '医保编码',
     '批准文号',
     '包装价格',
     '医保类型',
     '国家基药',
     '类型']

df_filtered.to_excel('D:\pythonProject\pythonProject\广东集采药品\广东集采药品.xlsx', index=False)
print('数据已写入表格，共计' + format(len(df)))
# 输出DataFrame

