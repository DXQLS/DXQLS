import requests
import pandas as pd

#设置允许跨域
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Content-Type': '*',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

data = {
    "medListCodg": "",
    "regName": "",
    "valiFlag": 1,
    "pageNum": 1,
    "pageSize": 10,
    'appId':'B2D051287CCC440AA35AC8A3A1A25DF7'
}

response = requests.post('https://ybj.hainan.gov.cn/ggfw/hsa-pss-pw/web/pw/terms/queryWmBypage',json=data,headers=headers, timeout=10)

print(response.json())
# def get_loop():
#     # 创建空列表存储所有数据
#     all_data = []
#     is_continue = True
#     while is_continue:
#
#         data_list = get_data()
#         all_data.extend(data_list['records'])
#         data["current"] += 1
#
#         print('正在爬取第'+ f'{data["current"]}' + '页的数据')
#         if len(data_list['records']) < 100:
#             data["current"] = 1
#             is_continue = False
#
#     return all_data
#
#
#
# def get_data():
#     for i in range(3):  # 尝试3次
#         try:
#             response = requests.post('https://open.ybj.fujian.gov.cn:10013/tps-local/web/tender/plus/item-cfg-info/list',json=data,headers=headers, timeout=10)
#             response.raise_for_status()  # 如果响应状态码不是200，抛出异常
#             datas = response.json()
#             data_list = datas['data']
#             return data_list
#         except requests.exceptions.ReadTimeout:
#             print("请求超时，正在重试...")
#
#
#
#
# if __name__ == '__main__':
#     all_data = get_loop()
#     # 创建 DataFrame 并打印
#     df = pd.DataFrame(all_data)
#     df_filtered = df[
#         ['druglistCode', 'druglistName', 'drugName', 'ruteName', 'dosformName', 'specName', 'pac', 'prodentpName']]
#     df_filtered.columns = ['目录号', '目录名称', '产品名称', '给药途径', '剂型', '通用规格', '通用包装', '挂网企业']
#     # print(df_filtered)
#     df_filtered.to_excel('D:\pythonProject\pythonProject\福建集采药品\福建集采药品.xlsx', index=False)
#     print('数据已写入表格，共计' + format(len(df)))