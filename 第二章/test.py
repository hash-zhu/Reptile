# csv文件与txt文件类似，区别点就是在csv文件中，字段间使用“, ”或“ | ”隔开，达到类似与表格的效果。
# csv文件可以使用记事本打开（打开可见分隔符“, ”），也可使用excel打开（打开以表格形式显示，看不见分隔符）。
# 注意：尽量不要使用wps打开，可能会打乱格式。

# 在操作csv文件时，需要导入csv库，csv是python内置库，无需下载

import csv

# 读取csv文件内容
# 在操作csv文件时，文件要保持打开状态，mode='r'表示操作模式为只读
cdata = open (r'./test.csv', mode='r', encoding='utf8')

# 以字符串形式进行读取，每次读取一行，返回结果包含分隔符
# for i in cdata:
#     print(i)#结果为字符串，如："1,3,5,7"

# 以列表形式进行读取，可使用循环遍历每一行读取
# clist=csv.reader(cdata)#注意：文件打开后每次只能进行一次操作
# for i in clist:
#     print(i)#结果为列表，列表内元素为字符串类型，如：['1', '3', '5', '7']


# 可将数据直接添加到列表中，方便后期使用
# result=[]#定义一个列表存储文件数据
# result.extend(clist)#将数据添加到列表中
# print(result)#[['1', '3', '5', '7'], ['2', '4', '6', '8']]

# 以字典形式进行读取，可使用循环遍历每一行读取
cdict = csv.DictReader(cdata)
for i in cdict:
    print ('%s,%s,%s,%s' % (i['l1'], i['l2'], i['l3'], i['l4']))
# cdata.close()#关闭文件

# 写入操作
# 对csv文件进行写入操作，mode='w'表示操作模式为只写，如文件不存在则自动创建文件覆盖写入
with open (r'./test2.csv', mode='w', newline='', encoding='utf8') as cf:
    wf = csv.writer (cf)
    wf.writerow (['name', 'age', 'sex'])
    data = [['小丽', '10', '女'], ['小李', '12', '男'], ['小力', '9', '男']]
    for i in data:
        wf.writerow (i)

# 末尾追加写入，文件必须已存在
with open (r'./test2.csv', mode='a', newline='', encoding='utf8') as cfa:
    wf = csv.writer (cfa)
    data2 = [['小美', '10', '女'], ['小力', '12', '男'], ]
    for i in data2:
        wf.writerow (i)
