import requests
import json
import pandas as pd

def get_yunnan_yuanneizhiji():
    is_continue = True
    all_list = []
    page_nums = 1
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://ylbz.yn.gov.cn",
        "Pragma": "no-cache",
        "Referer": "https://ylbz.yn.gov.cn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://ggfw.ynylbz.cn/hsa-pss-pw/web/pw/polcent/queryHilist"
    data = {
        "pageNum": 1,
        "pageSize": 90,
        "listType": 103,
        "usedCache": False,
        "hilistName": "",
        "hilistCode": ""
    }
    while is_continue:
        payloads = data.copy()
        payloads["pageNum"] = page_nums
        try:
            response = requests.post(url, headers=headers, json=payloads)
            datas = response.json()
            result_datas = datas['data']['list']
            all_list.extend(result_datas)
            print(f"返回数据{len(result_datas)}" + f"正在抓取第{page_nums}页数据" + f"共计爬取{len(all_list)}条数据")
            if len(result_datas) < 90:
                is_continue = False
            else:
                page_nums += 1
        except Exception as e:
            print(f"请求失败: {e}")
            break
    return all_list

if __name__ == '__main__':
    datas = get_yunnan_yuanneizhiji()
    df = pd.DataFrame(datas)

    df_filtered = df[
        ['hilistCode',
         'hilistUseType',
         'chrgitmLv',
         'hilistName',
         'dosform',
         'drugSpec',
         'pacmatl',
         'minPacunt',
         'minPrepunt',
         'minPacunt',
         'hospPrepAppyerEmpName',
         'aprvno'
         ]
    ]
    df_filtered.columns = [
        '医疗目录编码',
        '制剂类别',
        '医保目录等级',
        '制剂名称',
        '实际剂型',
        '实际规格',
        '包装材质',
        '最小包装数量',
        '最小包装单位',
        '最小制剂单位',
        '医疗机构名称',
        '批准文号'
    ]
    df_filtered.to_excel('D:\pythonProject\pythonProject\云南\云南药品_院内制剂.xlsx', index=False)

    print(f'数据已写入表格，共计{len(df_filtered)}条数据')

    print(len(datas))