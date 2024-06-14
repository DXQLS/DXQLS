import requests

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Content-Type': '*'
}
data = {
    'ylxmbm':'氯己定苯佐卡因含片',
    'page':1,
    'pageSize':10,
    'mllb':1,
    '__usersession_uuid':None,
    'XMLPara':' aEZJYlloVE1iSGxhUnVadmNnWkFzNGNSOVhNNWRrSEY0Qm1kZGZOeW53V2FzVStaZWsyeXE1U0E2VHY5Slg4ZCtDWk1tUWhnTUp4VFpkaFNmdzRSM3dXSEZld3BsV3IyUlBFeVdKSUYzSXF5SGRNZkFWVUNjaE5XK1hLK1BITkdIckljY3RISjh6U2dTQ1ZGSHFLRzNRQ3J6SDQ4ekJneGZLTUI0T1NCekFmZUdtclpWM2JiTW1DbUl1M1c3djFt',
    '_random:':'0.6015650229363845'
}

url = 'https://ybjggfw.yantai.gov.cn/SmartMISP/serv/Wb/queryMediItem'
data = requests.post(url=url,data=data,headers=headers)
print(data.text)

#醋酸氯己定溶液