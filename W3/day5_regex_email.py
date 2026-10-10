"""
该程序用于正则匹配邮箱地址
"""
import re
CONTENT_URL = """
 你好，相关资料可以发送至以下邮箱：
技术组：tech_support@example.com
个人联系：zhang.san-2026@mail.education.cn
备用邮箱：lisi@163.com
海外邮箱：amy.lee@google.org
请勿发送到这个无效邮箱：test@.com 以及 @wrong.com。
工作通知邮箱：work-9527@company-office.net
临时对接：wangwu@qq.com
请联系技术组zhang@example.com获取资料
甲乙@丙丁.com
 """

email_parte = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}')
for i in email_parte.findall(CONTENT_URL):
    print(i)

