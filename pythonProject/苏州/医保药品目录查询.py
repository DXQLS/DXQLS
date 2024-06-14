'''
Name : 医保药品目录查询.py
Author : WangShuZhou
Contact : 2443340977@qq.com
Time : 2024-06-14 13:41
'''
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd
import requests

headers = {
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Referer': 'https://ybj.suzhou.gov.cn/szybj/xhtml/ypmlQuery.html',
    'sec-ch-ua': '',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'sec-ch-ua-platform': '',
    'Cache-Control': 'no-cache',
    'Origin': 'https://ybj.suzhou.gov.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Mode': 'cors',
    'Cookie': 'wzws_sessionid=gWM5MmJhYYI0NjkxZDWgZmuY3oA2MC4xODYuOTEuMjI=; Hm_lvt_33235b88230452189f1c661467e21343=1718327519; arialoadData=true; ariawapChangeViewPort=false; Hm_lpvt_33235b88230452189f1c661467e21343=1718343608',
}
# 初始化列表
list_01, list_02, list_03, list_04, list_05, list_06, list_07, list_08, list_09, list_10, list_11, list_12, list_13, list_14, list_15, list_16 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []


def fetch_data(page_num):
    print(f"正在爬取{page_num}页")

    data = f'size=20&page={page_num}&name1=&name2=&code1=&code2=1'

    response = requests.post('https://ybj.suzhou.gov.cn/szinf/interfaceSbjjglzx/ybypmlcx', headers=headers, data=data)

    return json.loads(response.json())['data']['list']['info']


#
# print(data['data']['list']['info'])
def process_row(i):
    list_01.append(i.get('aka074', ''))
    list_02.append(i.get('aka064', ''))
    list_03.append(i.get('aka061', ''))
    list_04.append(i.get('aka070', ''))
    list_05.append(i.get('cme028', ''))
    list_06.append(i.get('aae100', ''))
    list_07.append(i.get('aka069', ''))
    list_08.append(i.get('cle006', ''))
    list_09.append(i.get('ake002', ''))
    list_10.append(i.get('ckb171', ''))
    list_11.append(i.get('cke330', ''))
    list_12.append(i.get('cke110', ''))
    list_13.append(i.get('bke208', ''))
    list_14.append(i.get('cke114', ''))
    list_15.append(i.get('cke115', ''))
    list_16.append(i.get('cke116', ''))


def main():
    num_pages = 6474  # 总页数，示例中使用10页
    max_workers = 5  # 最大并发线程数

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_page = {executor.submit(fetch_data, page_num): page_num for page_num in range(1, num_pages + 1)}
        for future in as_completed(future_to_page):
            page_num = future_to_page[future]
            try:
                rows = future.result()
                for row in rows:
                    process_row(row)
            except Exception as e:
                print(f'Error fetching page {page_num}: {e}')

    # 将列表数据转换为DataFrame
    df = pd.DataFrame({
        '药品名称': list_09,
        '中文通用名': list_03,
        '生产企业': list_08,
        '药品规格': list_01,
        '转换比': list_13,
        '包装材质': list_15,
        '单位': list_16,
        '药品剂型': list_04,
        'cme028': list_05,
        'aae100': list_06,
        'aka069': list_07,
        '处方药标志': list_02,
        '药品分类': list_10,
        'cke330': list_11,
        'cke114': list_14,
        '限定支付范围': list_12

    })

    # 将DataFrame保存到Excel文件
    df.to_excel("医保药品目录查询.xlsx", index=False)

    print("数据已成功保存到医保药品目录查询.xlsx")


if __name__ == "__main__":
    main()
