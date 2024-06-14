import pandas as pd
import requests

headers = {
    'Referer': 'https://fw.ybj.beijing.gov.cn/',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Sec-Fetch-Site': 'same-origin',
    'Origin': 'https://fw.ybj.beijing.gov.cn',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Cookie': '_va_id=db46c3d1fd2f7fc9.1715566969.2.1716176933.1716176894.; JSESSIONID=45C4023EDB6ED44E20D1404650615716; _va_ses=*; route=906b196178ecccc95c0c029dd8e377b0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0',
    'Priority': 'u=1',
    'Sec-Fetch-Mode': 'cors',
    'X-Requested-With': 'XMLHttpRequest',
}
ID_list = []  # 序号
Med_Names_list = []  # 药品名称
Med_No_list = []  # 药品编号
Limit_desc_list = []  # 药品说明
Med_Ser_list = []  # 药品类别
Med_dosage_list = []  # 药品剂型
DRUGPRICE_list = []
PROTOCOL_TIME_list = []
for i in range(1, 189):
    print(f"正在爬取第{i}页")
    data = 'line=1&levelnum=0&cpage=' + str(i)
    response = requests.post('https://fw.ybj.beijing.gov.cn/drug/druginfo/findChiledLimit', headers=headers, data=data)
    data = response.json()
    chiled = data['chiled']
    for c in chiled:
        ID = c['ID']
        ID_list.append(ID)
        Med_Names_list.append(c['DRUGNAME'])
        Med_No_list.append(c['DRUGNUMS'])
        Limit_desc_list.append(c['DRUGFACTS'])
        Med_Ser_list.append(c['DRUGTYPE'])
        Med_dosage_list.append(c['DRUGDOSAGE'])
        DRUGPRICE_list.append(c['DRUGPRICE'])
        PROTOCOL_TIME_list.append(c['PROTOCOL_TIME'])

all_dic = {'序号': ID_list, '药品名称': Med_Names_list, '药品编号': Med_No_list, '药品说明': Limit_desc_list, '药品类别': Med_Ser_list,
           '药品剂型': Med_dosage_list, 'DRUGPRICE': DRUGPRICE_list, 'PROTOCOL_TIME': PROTOCOL_TIME_list}

excel_dic = pd.DataFrame(all_dic)
excel_dic.to_excel("all.xlsx", index=False)
