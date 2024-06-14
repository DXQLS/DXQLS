import asyncio
import time

import aiohttp
import pandas as pd
async def fetch_data(regnCode):
    # 定义API请求的URL和payload模板
    url = f'https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/CommQuery/queryFixedHospital'
    payload_template = {
        "data": {
            "encData": "3DFBCA4667B978F639BB23B95DCE4CC74CE34C33DC32F1068E9E23CA546C9EA8CCD20943B4DAE96380B41164D761DE9742C84A985FE3BABC31CB352556BB87C9C1495DB24A29AB6BC3A85AB7FCA00F338EE714ACFC4C924F01CF575098AEF167B7A135B72DAC6C2F3CD510E411A3C63A9720F6A86E9EFCBA77082625D345D5DFD130FEBBE62DBFF03225CA796232EA15C36959880C2647559E3C97B56FD4F10F",
            "addr": "",
            "regnCode": regnCode,
            "medinsName": "",
            "medinsLvCode": "",
            "medinsTypeCode": "",
            "openElec": "",
            "pageNum": 1,
            "pageSize": 100,
            "queryDataSource": "es"
        },
        "encType": "SM4",
        "signData": "your_sign_data",
        "signType": "SM2",
        "timestamp": 1712110149,
        "version": "1.0.0",
    }

    async with aiohttp.ClientSession() as session:
        all_data = [] # 存储所有获取的数据的列表
        has_more_data = True # 是否还有更多数据的标志
        page_num = 1
        while has_more_data:
            payload = payload_template.copy()  # 复制payload模板
            payload["data"]["pageNum"] = page_num # 更新payload中的页码

            try:
                async with session.post(url, json=payload) as response:
                    response.raise_for_status() # 检查响应状态
                    data = await response.json() # 解析响应数据
                    current_data = data['data']['list'] # 提取当前页的数据
                    print(f"返回数据{len(current_data)}" + f"正在抓取第{page_num}页数据, {regnCode}")
                    for item in current_data:
                        item['arr_code'] = regnCode

                    all_data.extend(current_data) # 将当前页数据添加到all_data中
                    if len(current_data) < 100: # 如果返回数据小于100条，则表示没有更多数据
                        has_more_data = False
                    else:
                        page_num += 1
            except Exception as e:
                print(f"请求失败: {e}")
                break
        return all_data


async def main():
    code_list = pd.read_json('arr_code.json')['code']
    tasks = [fetch_data(regnCode) for regnCode in code_list] # 创建任务列表
    results = await asyncio.gather(*tasks) # 并发执行所有任务
    all_data = [item for sublist in results if sublist for item in sublist]  # 将结果扁平化成一维列表
    return all_data

if __name__ == '__main__':
    all_data = asyncio.run(main())
    df = pd.DataFrame(all_data)
    df_filtered = df[['arr_code','medinsName', 'medinsTypeName', 'medinsLvName', 'addr']]
    df_filtered.columns = ['地区编码','医疗机构名称', '医疗机构类型', '医疗机构等级', '详细地址']
    df_filtered.to_excel('D:\pythonProject\pythonProject\全国定点医院查询\全国定点医院机构查询.xlsx', index=False)
    print('数据已写入表格，共计' + format(len(df)))