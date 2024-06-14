'''
Name : 诊疗项目.py
Author : WangShuZhou
Contact : 2443340977@qq.com
Time : 2024-06-14 14:37
'''
from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd
import requests

headers = {
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Referer': 'https://ybj.suzhou.gov.cn/szybj/xhtml/zlxmQuery.html',
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
    'Cookie': 'wzws_sessionid=gWM5MmJhYYI0NjkxZDWgZmuY3oA2MC4xODYuOTEuMjI=; Hm_lvt_33235b88230452189f1c661467e21343=1718327519; arialoadData=true; ariawapChangeViewPort=false; Hm_lpvt_33235b88230452189f1c661467e21343=1718347024',
}

list_01, list_02, list_03, list_04, list_05, list_06, list_07, list_08, list_09, list_10, list_11, list_12 = ([] for _
                                                                                                              in
                                                                                                              range(12))


def fetch_data(page_num):
    print(f"正在爬取{page_num}页")
    data = f'size=20&page={page_num}&code=&name='
    # data = f'size=20&page={page_num}&name1=&name2=&code1=&code2=1'
    response = requests.post('https://ybj.suzhou.gov.cn/szinf/interfaceSbjjglzx/zlxmcx', headers=headers, data=data)

    return response.json()['data']['list']['info']


# 遍历数据列表，将数据添加到相应的列表中
def process_row(i):
    list_01.append(i.get('cke330', ''))
    list_02.append(i.get('bke107', ''))
    list_03.append(i.get('aaz231', ''))
    list_04.append(i.get('bke106', ''))
    list_05.append(i.get('cke464', ''))
    list_06.append(i.get('aab004', ''))
    list_07.append(i.get('cae586', ''))
    list_08.append(i.get('aka069', ''))
    list_09.append(i.get('cke456', ''))
    list_10.append(i.get('bke146', ''))
    list_11.append(i.get('bke145', ''))
    list_12.append(i.get('ake002', ''))


def main():
    num_pages = 464  # 总页数，示例中使用10页
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
        'cke330': list_01,
        'bke107': list_02,
        'aaz231': list_03,
        'bke106': list_04,
        'cke464': list_05,
        'aab004': list_06,
        'cae586': list_07,
        'aka069': list_08,
        'cke456': list_09,
        'bke146': list_10,
        'bke145': list_11,
        'ake002': list_12
    })

    # 将DataFrame保存到Excel文件
    df.to_excel("诊疗项目.xlsx", index=False)

    print("诊疗项目.xlsx")


if __name__ == "__main__":
    main()
