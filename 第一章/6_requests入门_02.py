import requests

url = 'https://fanyi.baidu.com/sug'
input_str = input("请输入您要翻译的单词：")
data = {"kw": input_str}

resp = requests.post(url=url, data=data)
# 发送post请求,发送的数据必须放在字典中，通过data参数进行传参
print(resp.json())#将服务器返回的内容直接处理成json()=>dict
