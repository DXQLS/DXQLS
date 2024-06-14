import pandas as pd
import requests
from lxml import etree

'index.jsp?field=vc_name:1:0,field_28148:1:0&i_columnid=97806&vc_name=&field_28148=&currpage=5'

headers = {
    'Referer': 'http://ybj.shandong.gov.cn/col/col97806/index.html',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Upgrade-Insecure-Requests': '1',
    'Cookie': 'zh_choose_358=s; _gscu_143548366=161850535r2ig540; _gscbrs_143548366=1; _gscs_143548366=161850532nx74540|pv:1; wondersLog_sdywtb_sdk=%7B%22persistedTime%22%3A1716185053172%2C%22updatedTime%22%3A1716185054556%2C%22sessionStartTime%22%3A1716185054555%2C%22sessionReferrer%22%3A%22%22%2C%22deviceId%22%3A%225f37ae3f8638a9ac66dc1ac2d18de7c5-8243%22%2C%22LASTEVENT%22%3A%7B%22eventId%22%3A%22wondersLog_pv%22%2C%22time%22%3A1716185054556%7D%2C%22sessionUuid%22%3A6852490067444450%2C%22costTime%22%3A%7B%22wondersLog_unload%22%3A1716185054556%7D%7D',
    'Cache-Control': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Pragma': 'no-cache',
    'Connection': 'keep-alive',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

code_list = []
name_list = []
station_list = []
series_list = []
level_list = []
No6_list = []
No7_list = []
for i in range(1, 4):
    print(f"正在爬取第{i}页数据")
    url = 'http://ybj.shandong.gov.cn/module/search/index.jsp?field_28148=&vc_name=&strSelectID=28148%2C28104&i_columnid=97806&field=vc_name%3A1%3A0%2Cfield_28148%3A1%3A0&initKind=FieldForm&type=0%2C0&currentplace=&splitflag=&fullpath=0&download=%E6%9F%A5%E8%AF%A2&currpage=' + str(
        i)
    response = requests.get(url, headers=headers)

    with open("1.html", "w", encoding="utf-8") as fp:
        fp.write(response.text)
    html = etree.HTML(response.text)
    # print(html.xpath('/html/body/table[2]/tr[1]//text()'))
    # print(response.text)  '/html/body/table[2]/tbody'
    t_body_path = html.xpath('/html/body/table[2]/tr')  # '/html/body/table[2]/tbody'
    # '/html/body/table[2]/tbody/tr[1]
    # print(t_body_path)
    # '/html/body/table[2]/tbody/tr[1]/td/table/tbody'
    # print(len(t_body_path))
    for tr in t_body_path:
        # print(tr.xpath('.//text()'))
        # print(tr.xpath('./td/table/tr//text()'))
        # '/html/body/table[2]/tbody/tr[1]'
        # '/html/body/table[2]/tbody/tr[1]/td/table/tbody/tr'
        # for td in tr.xpath('./td/table/tbody/tr/td'):
        for td in tr.xpath('./td/table/tr'):
            # print(td.xpath('.//text()'))
            # print(td)
            code = td.xpath('./td[1]/text()')[0]
            name = td.xpath('./td[2]/text()')[0]
            station = td.xpath('./td[3]/text()')[0]
            series = td.xpath('./td[4]/text()')[0]
            level = td.xpath('./td[5]/text()')[0]
            No_6 = td.xpath('./td[6]/text()')[0]
            No_7 = td.xpath('./td[7]/text()')[0]
            code_list.append(code)
            name_list.append(name)
            station_list.append(station)
            series_list.append(series)
            level_list.append(level)
            No6_list.append(No_6)
            No7_list.append(No_7)
to_execl_dic = {"编号": code_list, "医院名称": name_list, "所属区": station_list, "医院类别": series_list, "医院等级": level_list,
                'No6': No6_list, 'No7': No7_list}

to_execl_dic = pd.DataFrame(to_execl_dic)
print(to_execl_dic)
# to_execl_dic.to_excel("山东table1.xlsx", index=False)
