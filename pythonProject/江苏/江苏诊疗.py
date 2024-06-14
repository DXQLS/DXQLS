'''
Name : 江苏省医保诊疗信息查询.py
Author : WangShuZhou
Contact : 2443340977@qq.com
Time : 2024-05-27 10:15
'''
import json
import re

ILLEGAL_CHARACTERS_RE = re.compile(r'[\000-\010]|[\013-\014]|[\016-\037]')

with open('江苏省医保诊疗信息查询_copy.txt', 'r+', encoding='utf8') as fp:
    data = fp.read()
    # print(data)
datas = json.loads(data)
code_list = []
item_name_list = []
nationItemCode_list = []
nationItemName_list = []
itemContent_list = []
exceptContent_list = []
payType_list = []
priceUnit_list = []
threeHospPriceSouth_list = []
threeHospPriceMiddle_list = []
threeHospPriceNorth_list = []
twoHospPriceSouth_list = []
twoHospPriceMiddle_list = []
twoHospPriceNorth_list = []
oneHospPriceSouth_list = []
oneHospPriceMiddle_list = []
oneHospPriceNorth_list = []
provide_list = []
memo_list = []
price_constr_list = []
service_product_list = []
for data in datas:
    list_data = data['data']['list']
    for i in list_data:
        code = i['tollItemCode']
        code_list.append(code)
        item_name = i['tollItemName']
        item_name_list.append(item_name)
        nationItemCode = i['nationItemCode']
        nationItemCode_list.append(nationItemCode)
        nationItemName = i['nationItemName']
        nationItemName_list.append(nationItemName)
        try:
            itemContent = i['itemContent']
            itemContent_list.append(itemContent)
        except:
            itemContent_list.append("")
        try:
            exceptContent = i['exceptContent']
            exceptContent_list.append(exceptContent)
        except:
            exceptContent_list.append("")

        payType_list.append(i['payType'])
        priceUnit_list.append(i['priceUnit'])
        try:
            threeHospPriceSouth_list.append(i['threeHospPriceSouth'])
        except:
            threeHospPriceSouth_list.append(" ")
        try:
            threeHospPriceMiddle_list.append(i['threeHospPriceMiddle'])
        except:
            threeHospPriceMiddle_list.append(" ")
        try:
            threeHospPriceNorth_list.append(i['threeHospPriceNorth'])
        except:
            threeHospPriceNorth_list.append(" ")
        try:
            twoHospPriceSouth_list.append(i['twoHospPriceSouth'])
        except:
            twoHospPriceSouth_list.append(" ")
        try:
            twoHospPriceMiddle_list.append(i['twoHospPriceMiddle'])
        except:
            twoHospPriceMiddle_list.append(" ")
        try:
            twoHospPriceNorth_list.append(i['twoHospPriceNorth'])
        except:
            twoHospPriceNorth_list.append(" ")
        try:
            oneHospPriceSouth_list.append(i['oneHospPriceSouth'])
        except:
            oneHospPriceSouth_list.append(" ")
        try:
            oneHospPriceMiddle_list.append(i['oneHospPriceMiddle'])
        except:
            oneHospPriceMiddle_list.append(" ")
        try:
            oneHospPriceNorth_list.append(i['oneHospPriceNorth'])
        except:
            oneHospPriceNorth_list.append("")
        provide_list.append("--")
        try:

            memo = i['memo']
            memo_list.append(memo)
            # if memo > 20:
            #     memo_list.append(memo)
            # else:
            #     memo_list.append("数据过长")
            # memo = ILLEGAL_CHARACTERS_RE.sub(r'', memo)
        except:
            memo_list.append(" ")
        service_product_list.append("--")
        price_constr_list.append("--")

all_dic = {'收费项目编码': code_list, '收费项目名称': item_name_list, '国家医疗服务项目代码': nationItemName_list,
           '国家医疗服务项目名称': nationItemName_list, '项目内涵': itemContent_list, '除外内容': exceptContent_list,
           '医保支付类别': payType_list, '计价单位': priceUnit_list, '三类苏南': threeHospPriceSouth_list,
           '三类苏中': threeHospPriceMiddle_list, '三类苏北': threeHospPriceNorth_list, '二类苏南': twoHospPriceSouth_list,
           '二类苏中': twoHospPriceMiddle_list, '二类苏北': twoHospPriceNorth_list, '一类苏南': oneHospPriceSouth_list,
           '一类苏中': oneHospPriceMiddle_list, '一类苏南': oneHospPriceSouth_list, '一类苏中': oneHospPriceMiddle_list,
           '一类苏北': oneHospPriceNorth_list, '供应价格': provide_list, '说明': memo_list, '服务产出': service_product_list,
           '价格构成': price_constr_list}
import pandas as pd

all_dic = pd.DataFrame(all_dic)
all_dic.index = all_dic.index + 1
all_dic.to_excel('江苏省医保诊疗信息查询.xlsx')
#     pass
