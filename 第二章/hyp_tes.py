import re
import requests
import csv

url ="http://cyds.hnszhzjs.org.cn:8080/"

resp = requests.get(url)

print(resp.text)