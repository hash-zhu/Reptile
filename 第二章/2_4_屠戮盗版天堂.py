# 1.定位到2021必看片
# 2.从2021必看片中提取到子页面的链接地址
# 3.请求子页面的链接地址，拿到我们想要的下载地址....

import requests
import re

domain = "https://www.dytt89.com/"
# resp = requests.get(domain, verify=False)# verify=False 去掉安全链接
resp = requests.get (domain)
resp.encoding = "gb2312"  # 指定字符集
# print(resp.text)

# 拿到 ul 里面的 li
obj1 = re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<li><a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名　   (?P<name>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<downloadUrl>.*?)"',re.S)
result1 = obj1.finditer(resp.text)
child_list = []
for it in result1:
    ul = it.group('ul')
    # print(ul)
    # 提取子页面链接：
    result2 = obj2.finditer(ul)
    for itt in result2:
        # 拼接子页面的url地址：  域名 + 子页面地址
        child_href = domain + itt.group('href').strip("/")
        child_list.append(child_href)
        # print(child_href)
        # print(itt.group("href"))

# 提取子页面内容
for href in child_list:
    child_resp = requests.get(href)
    child_resp.encoding = "gb2312"
    # print(child_resp.text)
    items = obj3.finditer(child_resp.text)
    for it in items:
        name = it.group("name")
        print(name)
        downloadUrl = it.group("downloadUrl")
        print(downloadUrl)
    break # 测试用
