
"""
输入：字典：键值访问、遍历、get、in
动手：词频雏形
当天过关题：输入一句话，输出每个字出现的次数（用 dict）
"""

sentence = input("请输入一句话：")
char_count = {}
for char in sentence:
    # if char != " " and char != '，':
        # if char in char_count:
    if  char.isalpha():
            char_count[char] = char_count.get(char,0)+1

sort_char_count = sorted(char_count.items(),key=lambda item:item[1],reverse=True)
print(sort_char_count)
