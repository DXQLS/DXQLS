import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import time
# 设置允许跨域
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Content-Type': '*'
}



max_page = 500
num_threads = 5  # 设置线程数

def fetch_data(page):
    url = f'https://ybj.hainan.gov.cn/tps-local/local/web/std/queryService/queryMcsPubRsltPage?current={page}&size=50'
    response = requests.get(url=url, headers=headers,timeout=10)
    time.sleep(1)
    data = response.json()
    datas = data['data']['records']
    print(f'正在爬取第{page}页数据')
    return datas


with ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = [executor.submit(fetch_data, page) for page in range(1, max_page + 1)]
    all_data = []
    for future in futures:
        data_chunk = future.result()
        all_data.extend(data_chunk)
        chunk_df = pd.DataFrame(data_chunk)
        chunk_df = chunk_df[
            ['mcsCode', 'mcsName', 'prodentpName', 'mcsRegno', 'mcsSpec', 'mcsMatl', 'pubonlnPric']
        ]
        chunk_df.columns = ['耗材统一编码', '耗材名称', '生产企业', '注册证编号', '规格', '材质', '挂网价格']
        # all_data = pd.concat([all_data, pd.DataFrame(data_chunk)], ignore_index=True)
    chunk_df.to_excel('D:\pythonProject\pythonProject\海南药品耗材集采\海南耗材集采_500.xlsx', index=False)
    # write_to_excel(all_data)
    print('数据爬取完成并写入表格' + f'{len(all_data)}')
