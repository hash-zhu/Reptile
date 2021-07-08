# 安装
#  pip install bs4 -i 清华

# 1.拿到页面源代码
# 2.使用bs4进行解析，拿到数据
import requests

url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
resp = requests.get(url)
print(resp.text)