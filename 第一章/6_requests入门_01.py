# 安装requests
# pip install requests
# 国内源  __ 清华
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
import requests

query = input()
url = f"https://www.sogou.com/web?query={query}"

header ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
          }
# 处理一个小小的反爬
resp = requests.get(url, headers=header)
print(resp)
print(resp.text) # 拿到页面代码
