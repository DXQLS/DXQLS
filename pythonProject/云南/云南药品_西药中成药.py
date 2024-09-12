import requests
import json
import pandas as pd




def get_yunnan_yuanneizhiji():
    is_continue = True
    all_list = []
    page_nums = 1
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://ggfw.ynylbz.cn",
        "Pragma": "no-cache",
        "Referer": "https://ggfw.ynylbz.cn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "Hm_lvt_2e9e12b673ad61053eabf1dbc33f8217": "1725954024,1726037691",
        "HMACCOUNT": "1E14B2327DDD5FAB",
        "SESSION_FLAG": "2",
        "Hm_lpvt_2e9e12b673ad61053eabf1dbc33f8217": "1726037731",
        "headerShow": "false"
    }
    url = "https://ggfw.ynylbz.cn/hsa-pss-pw/web/pw/polcent/queryHilist"
    data = {
        "listType": "101",
        "hilistCode": "",
        "regName": "",
        "drugGenname": "",
        "valiFlag": 1,
        "pageNum": 1,
        "pageSize": 50,
        "usedCache": False
    }
    while is_continue:
        payloads = data.copy()
        payloads["pageNum"] = page_nums
        try:
            response = requests.post(url, headers=headers,cookies=cookies, json=payloads)
            datas = response.json()
            result_datas = datas['data']['list']
            all_list.extend(result_datas)
            print(f"返回数据{len(result_datas)}" + f"正在抓取第{page_nums}页数据" + f"共计爬取{len(all_list)}条数据")
            if len(result_datas) < 50:
                is_continue = False
            else:
                page_nums += 1
        except Exception as e:
            print(f"请求失败: {e}")
            continue
    return all_list

if __name__ == '__main__':
    datas = get_yunnan_yuanneizhiji()
    df = pd.DataFrame(datas)

    df_filtered = df[
        ['medListCodg',
         'chrgitmLv',
         'regDosform',
         'drugDosform',
         'regSpec',
         'pacmatl',
         'minPacCnt',
         'minPacunt',
         'minPrepunt',
         'prodentpName',
         'aprvno'
         ]
    ]
    df_filtered.columns = [
        '医疗目录编码',
        '医保目录等级',
        '注册剂型',
        '实际剂型',
        '注册规格',
        '包装材质',
        '最小包装数量',
        '最小包装单位',
        '最小制剂单位',
        '药品企业',
        '批准文号'

    ]
    df_filtered.to_excel('D:\pythonProject\pythonProject\云南\云南药品_西药中成药.xlsx', index=False)

    print(f'数据已写入表格，共计{len(df_filtered)}条数据')