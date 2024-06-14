import requests
import pandas as pd

#设置允许跨域
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Content-Type': '*'
}

data = {
    "current": 1,
    "size": 40
}

def get_loop():
    # 创建空列表存储所有数据
    all_data = []
    is_continue = True
    while is_continue:

        data_list = get_data()
        all_data.extend(data_list['records'])
        print(data_list['records'])
        data["current"] += 1

        print('正在第爬取'+ f'{data["current"]}' + '页的数据')
        if len(data_list['records']) < 40:
            data["current"] = 1
            is_continue = False

    return all_data




def get_data():
    for i in range(3):  # 尝试3次
        try:
            response = requests.post('https://fuwu.pubs.ylbzj.guizhou.gov.cn/hsa-pss-hall/pss/hall/web/enter/zcPublic/queryMedConsuList',json=data,headers=headers, timeout=10)
            response.raise_for_status()  # 如果响应状态码不是200，抛出异常
            datas = response.json()
            data_list = datas['data']
            return data_list
        except requests.exceptions.ReadTimeout:
            print("请求超时，正在重试...")




if __name__ == '__main__':
    all_data = get_loop()
    # 创建 DataFrame 并打印
    df = pd.DataFrame(all_data)
    # df_filtered = df[['prodCode','prodName', 'aprvno']]
    df.columns = ['医保编码', '医用耗材单件产品名称', '注册证号']
    # print(df_filtered)
    df.to_excel('D:\pythonProject\pythonProject\贵州药品耗材集采\贵州耗材集采.xlsx', index=False)
    print('数据已写入表格，共计' + format(len(df)))
