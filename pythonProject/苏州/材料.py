'''
Name : 材料.py
Author : WangShuZhou
Contact : 2443340977@qq.com
Time : 2024-06-14 14:39
'''

from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd
import requests

headers = {
    'Referer': 'https://ybj.suzhou.gov.cn/szybj/yycl/yycl.shtml',
    'sec-ch-ua': '',
    'Accept': '*/*',
    'Sec-Fetch-Dest': 'empty',
    'sec-ch-ua-platform': '',
    'Cookie': 'wzws_sessionid=gWM5MmJhYYI0NjkxZDWgZmuY3oA2MC4xODYuOTEuMjI=; Hm_lvt_33235b88230452189f1c661467e21343=1718327519; arialoadData=true; ariawapChangeViewPort=false; Hm_lpvt_33235b88230452189f1c661467e21343=1718347024',
    'Sec-Fetch-Site': 'same-origin',
    'sec-ch-ua-mobile': '?0',
    'X-Requested-With': 'XMLHttpRequest',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Pragma': 'no-cache',
    'Sec-Fetch-Mode': 'cors',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}


def fetch_data(page_num):
    print(f"正在爬取{page_num}页")
    response = requests.get(
        f'https://ybj.suzhou.gov.cn/szinf/interfacesWebYbjYyhc/loadPage?title=&clpp=&bdbm=&ygcgptbh=&currpage={page_num}&pagesize=10',
        headers=headers)
    return response.json()['data']['list']


# 初始化列表
# 初始化列表
list_01, list_02, list_03, list_04, list_05, list_06, list_07, list_08, list_09, list_10, list_11, list_12, list_13, list_14, list_15, list_16, list_17, list_18, list_19, list_20, list_21, list_22, list_23, list_24, list_25, list_26, list_27, list_28, list_29, list_30, list_31, list_32, list_33, list_34, list_35 = (
    [] for _ in range(35))


# 遍历数据列表，将数据添加到相应的列表中
def process_row(i):
    list_01.append(i.get('GJHCFLDM', ''))
    list_02.append(i.get('ZGZFBL', ''))
    list_03.append(i.get('CLXH', ''))
    list_04.append(i.get('SMLBM', ''))
    list_05.append(i.get('YD', ''))
    list_06.append(i.get('CLCJ', ''))
    list_07.append(i.get('SEZFBL', ''))
    list_08.append(i.get('SJYY', ''))
    list_09.append(i.get('BDBM', ''))
    list_10.append(i.get('HLY', ''))
    list_11.append(i.get('XYTXMT', ''))
    list_12.append(i.get('YBMLBM', ''))
    list_13.append(i.get('CLGG', ''))
    list_14.append(i.get('CLZLCC', ''))
    list_15.append(i.get('LXZFXJ', ''))
    list_16.append(i.get('YJYY', ''))
    list_17.append(i.get('id', ''))
    list_18.append(i.get('CLSM', ''))
    list_19.append(i.get('SQ', ''))
    list_20.append(i.get('CLMC', ''))
    list_21.append(i.get('JFDJ', ''))
    list_22.append(i.get('EJYY', ''))
    list_23.append(i.get('YBZFBZ', ''))
    list_24.append(i.get('SYZFBL', ''))
    list_25.append(i.get('xh', ''))
    list_26.append(i.get('LXZFBL', ''))
    list_27.append(i.get('BNZMT', ''))
    list_28.append(i.get('MZB', ''))
    list_29.append(i.get('CLPP', ''))
    list_30.append(i.get('WSS', ''))
    list_31.append(i.get('JLDW', ''))
    list_32.append(i.get('SFDB', ''))
    list_33.append(i.get('YGCGPTBH', ''))
    list_34.append(i.get('ZS', ''))
    list_35.append(i.get('ZCZH', ''))


def main():
    num_pages = 4401  # 总页数，示例中使用10页
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
        'GJHCFLDM': list_01,
        'ZGZFBL': list_02,
        'CLXH': list_03,
        'SMLBM': list_04,
        'YD': list_05,
        'CLCJ': list_06,
        'SEZFBL': list_07,
        'SJYY': list_08,
        'BDBM': list_09,
        'HLY': list_10,
        'XYTXMT': list_11,
        'YBMLBM': list_12,
        'CLGG': list_13,
        'CLZLCC': list_14,
        'LXZFXJ': list_15,
        'YJYY': list_16,
        'id': list_17,
        'CLSM': list_18,
        'SQ': list_19,
        'CLMC': list_20,
        'JFDJ': list_21,
        'EJYY': list_22,
        'YBZFBZ': list_23,
        'SYZFBL': list_24,
        'xh': list_25,
        'LXZFBL': list_26,
        'BNZMT': list_27,
        'MZB': list_28,
        'CLPP': list_29,
        'WSS': list_30,
        'JLDW': list_31,
        'SFDB': list_32,
        'YGCGPTBH': list_33,
        'ZS': list_34,
        'ZCZH': list_35
    })

    # 将DataFrame保存到Excel文件
    df.to_excel("材料.xlsx", index=False)

    print("数据已成功保存到材料.xlsx")


if __name__ == "__main__":
    main()
