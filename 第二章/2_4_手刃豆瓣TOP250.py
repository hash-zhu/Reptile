# 拿到页面源代码    request
# 通过re来提取想要的有效信息 re
import requests
import re
import csv

start = 25


def get_douban(start) -> str:
    url = f"https://movie.douban.com/top250/?start={start}&filter="
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36"
    }
    resp = requests.get (url, headers=header)
    # print(resp.text)

    # 开始匹配
    page_content = resp.text
    # 存储文件
    # f = open("data.csv", mode="w",encoding="utf-8-sig",newline='')
    # model="a" ：即在末尾追加写入，文件必须已存在
    with open ("data.csv", mode="a", encoding="utf-8-sig", newline='') as f:
        csvWriter = csv.writer (f)
        obj = re.compile (r' <li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
                          r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                          r'.*?<span>(?P<num>.*?)人评价</span>', re.S)

        resp = obj.finditer(page_content)
        for i in resp:
            # print(i.group("name"))
            # print(i.group('score'))
            # print(i.group('num'))
            # print(i.group("year").strip()).
            dic = i.groupdict()
            dic['year'] = dic['year'].strip()
            csvWriter.writerow(dic.values())


print ("over!")
