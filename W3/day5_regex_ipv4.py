"""
该程序主要使用正则表达式匹配IP v4地址
"""
import re
CONTENT_URL = """
192.168.1.1
10.0.0.1
172.16.0.1
192.168.1.100
10.0.0.255
172.16.0.100
"""
seg = r'(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
ip_parte = re.compile(rf'(?<![\d.]){seg}(?:\.{seg}){{3}}(?![\d.])')


for i in ip_parte.findall(CONTENT_URL):
    print(i)

