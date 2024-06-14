import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import time

# 设置允许跨域
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Content-Type': '*'
}


def fetch_data(page):
    url = f'https://ybj.hainan.gov.cn/tps-local/local/web/std/queryService/queryDrugPubRsltPageGs?current={page}&size=50'
    response = requests.get(url=url, headers=headers)
    data = response.json()
    return data['data']['records']


if __name__ == '__main__':
    max_page = 358
    start_time = time.time()
    all_data = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fetch_data, page) for page in range(1, max_page + 1)]
        for idx, future in enumerate(futures, 1):
            data = future.result()
            all_data.extend(data)
            if idx % 10 == 0:  # 每爬取10页打印一次
                print(f'正在爬取第{idx}页数据，目前共计爬取{len(all_data)}条')

    df = pd.DataFrame(all_data, columns=[
        'drugCode', 'drugName', 'dosformName', 'pac', 'specName',
        'aprvno', 'prodentpName', 'pubonlnPric', 'tbjj', 'isYzxpj', 'isprice'
    ])
    df.columns = [
        '药品统一编码', '药品名称', '剂型', '包装', '规格', '批准文号',
        '生产企业', '挂网价格', '是否中选', '是否过一次性评价', '是否可议价'
    ]
    df.to_excel('D:\pythonProject\pythonProject\海南药品耗材集采\海南药品集采.xlsx', index=False)

    print(f'数据已写入表格，共计{len(df)}条，耗时{time.time() - start_time}秒')
