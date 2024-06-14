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
