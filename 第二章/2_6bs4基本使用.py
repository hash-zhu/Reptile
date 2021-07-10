# 安装
#  pip install bs4 -i 清华

# 1.拿到页面源代码
# 2.使用bs4进行解析，拿到数据
import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
resp = requests.get(url)
# print(resp.text)

f = open("菜价.csv", mode="w", encoding="utf-8", newline="")
csvWriter = csv.writer(f)
# 解析数据
# 1.把页面源代码交给BeautifulSoup进行处理，生成bs对象
page = BeautifulSoup (resp.text, features="html.parser")  # 指定html解析器
# 2.从bs对象中查找数据
# find(标签名，属性=值)
# find_all(标签名，属性=值)
# table = page.find("table",class_="hq_table") # class是python的关键字
table = page.find ("table", attrs={"class": "hq_table"})  # class_是避免关键字不能使用的问题
# print (table)
# 拿到所有的数据行，去除表头
trs = table.find_all("tr")[1:]
for tr in trs:
    tds = tr.find_all("td")  # 每行中的所有td
    name = tds[0].text  # .text 表示拿到被标签标记的内容
    low = tds[1].text  # .text 表示拿到被标签标记的内容
    avg = tds[2].text  # .text 表示拿到被标签标记的内容
    high = tds[3].text  # .text 表示拿到被标签标记的内容
    gui = tds[4].text  # .text 表示拿到被标签标记的内容
    kind = tds[5].text  # .text 表示拿到被标签标记的内容
    date = tds[6].text  # .text 表示拿到被标签标记的内容
    csvWriter.writerow([name, low, avg, high, gui, kind, date])

f.close()
print("over!!!")