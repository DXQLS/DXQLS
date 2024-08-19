import requests as re

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Content-Type': '*',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}


url = 'https://oagate.ebaolife.net/tpa-sc/api/preReceive?limit=10&page=1&startRegisterDate=&endRegisterDate='
data = {
    'limit':10,
    'page':1
    }



data = re.get(url = url,json=data,headers= headers)

print(data.json())