'''
Name : test2.py
Author : WangShuZhou
Contact : 2443340977@qq.com
Time : 2024-04-30 16:35
'''
import re

import pandas as pd
import requests
from lxml import etree

headers = {
    'Referer': 'https://code.nhsa.gov.cn/jbzd/public/dataWesterSearch.html?batchNumber=',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Dest': 'iframe',
    'Upgrade-Insecure-Requests': '1',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Sec-Fetch-Site': 'same-origin',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Cookie': 'https_waf_cookie=23ca82d2-5293-43438e88d49d7c8e6d49b02c185ed02b098f; JSESSIONID=BD414DBE0B9D20B59F59CD27245DD070',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Connection': 'keep-alive',
    'Sec-Fetch-Mode': 'navigate',
    'Origin': 'https://code.nhsa.gov.cn',
}


def GetIcdId():
    IcdId_list = []
    headers = {
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate, br',
        'Sec-Fetch-Dest': 'document',
        'Upgrade-Insecure-Requests': '1',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
        'Cookie': 'https_waf_cookie=23ca82d2-5293-43438e88d49d7c8e6d49b02c185ed02b098f; JSESSIONID=6126F528E5EDB40FC3CF5D20AC7AFE4B',
        'Sec-Fetch-Mode': 'navigate',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    }
    resp = requests.get('https://code.nhsa.gov.cn/jbzd/public/toStdIcdTreeList.html', headers=headers)
    # print(resp.json())
    data = resp.json()
    # print(len(data))
    for _ in data:
        IcdId_list.append(_["icdId"])
        # print(_["icdId"])
    return IcdId_list


def To_excel():
    IcdId_list = GetIcdId()
    code = []
    name = []
    parent = []
    for icdId in IcdId_list:
        data = 'icdId=%5B%22' + icdId + '%22%5D&params='
        response = requests.post('https://code.nhsa.gov.cn/jbzd/public/toStdIcdDetail.html', headers=headers, data=data)
        # print(response.text)
        with open("3.html", "w+", encoding="utf-8") as fp:
            fp.write(response.text)
        html = etree.HTML(response.text)
        div_path = html.xpath('//*[@id="classicont"]')
        for div in div_path:
            # print(div.xpath('.//a/@href'))  # 原始数据
            # print(div.xpath('.//text()'))
            content = div.xpath('.//text()')
            pattern = re.compile(r'\n.*')
            content = [c for c in content if not pattern.match(c)]
            pattern = re.compile(r'.*\r\n')
            content = [c for c in content if not pattern.match(c)]
            content = [c.strip() for c in content]
        # content_end = []
        # for c in content:
        #     c = c.tr
        #     print(c)
        #     content_end.append(c)
        with open("4.html", "w+", encoding="utf-8") as fp:
            fp.write(str(content))

        toexcel_dir = {}

        first_par = ''
        last_par = ''
        previous_par = ''  # 新增最新变量  防止出现 A00 A00.001 A000.001X001 A00.001X002应该为 A00.001但是不使用pre变量会出现
        first_last_par = ''
        for i in range(2, len(content), 2):
            now_code = content[i]
            code.append(now_code)
            now_name = content[i + 1]
            name.append(now_name)
            if first_par != '':
                if (first_par in now_code and first_par != now_code) or (
                        last_par in now_code and last_par != now_code) or (
                        previous_par in now_code and previous_par != now_code) or (
                        first_last_par in now_code and first_last_par != now_code):
                    if last_par in now_code:
                        parent.append(last_par)
                        previous_par = last_par
                        last_par = now_code
                        continue
                    if previous_par in now_code:
                        parent.append(previous_par)
                        last_par = now_code
                        continue
                    if first_last_par in now_code:
                        parent.append(first_last_par)
                        continue
                    if first_par in now_code:
                        last_par = now_code
                        previous_par = first_par
                        parent.append(first_par)
                        continue
                else:
                    first_par = now_code
                    last_par = now_code
                    if i + 2 <= len(content) - 1:
                        first_last_par = content[i + 2]
                    print(first_last_par)
                    parent.append("")
            else:
                first_par = now_code
                last_par = now_code
                first_last_par = content[i + 2]
                print(first_last_par)
                parent.append("")
    print(parent)
    print(len(parent), len(name))
    toexcel_dir = {"code": code, "name": name, "parent": parent}
    toexcel_dir = pd.DataFrame(toexcel_dir)
    toexcel_dir.to_excel("code_name.xlsx", index=False)


if __name__ == '__main__':
    To_excel()
    # IcdIds = GetIcdId()
    # for i in IcdIds:
    #     print(i)
