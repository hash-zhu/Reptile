import requests

url = 'https://movie.douban.com/j/chart/top_list'

# 重新封装参数
param = {
    'type': 24,
    'interval_id': "100:90",
    "action": '',
    "start": '0',
    'limit': '20'
}
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36'
}
resp = requests.get(url=url, params=param, headers=header)

print(resp.request.url)
print(resp.request.headers)
print(resp.json ())
resp.close()  # 关掉resp
