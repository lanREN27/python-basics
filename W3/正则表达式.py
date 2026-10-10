import re
#
# with open("resource/text.txt","r",encoding="utf-8") as f :
#     text = f.read()
#
# content = re.compile(r'([\d.]+)万/每?月')
# result = content.findall(text)
# for i in result:
#     print(i)

content = """
001-苹果价格-60
002-橙子价格-70
003-香蕉价格-90
"""
p = re.compile(r'^\d+',re.MULTILINE)#compile 编译正则表达式
result = p.findall(content)
for i in result:

    print(i)

#. 表示任意字符
#*表示匹配前一个字符任意次，包括0次
#色*，表示匹配色任意次，包括0次 例如 r'绿色*' 则哪怕是单独一个‘绿’也会匹配
#+，则表示前面的字符至少出现一次

#{}表示前面的字符匹配指定的次数，例如：油{3,4}，表示匹配油至少三次，至多4次
# ?表示前面的字符最多出现一次，非贪婪模式，尽可能少的去匹配
#$表示字符串的结束，例如 r'价格$'，则只有当价格出现在字符串的末尾时才会匹配
#^表示字符串的开始，例如 r'^价格'，则只有当价格出现在字符串的开头时才会匹配
# \d 表示匹配任意数字，\D 表示匹配任意非数字
# \s 表示匹配任意空白字符，\S 表示匹配任意非空白字符
# \w 表示匹配任意字母数字字符，\W 表示匹配任意非字母数字字符

