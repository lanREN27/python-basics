"""
遍历 1～30 的所有整数；
如果数字是 3 的倍数，跳过本次循环（不要打印）；
如果数字大于 25，直接终止整个循环；
其余数字正常打印；
额外要求：先用 for + range 实现一遍，再用 while 实现一遍
"""
# for i in range(1,31):
#     if i%3==0:
#         continue
#     if i>25:
#         break
#
#     print(i)

#
# i=1
# while i<31 and i>0:
#     if i % 3 == 0:
#         i+=1
#         continue
#     if i > 25:
#         break
#     print(i)
#     i+=1

"""
模拟用户登录场景：
用户最多有3 次输入密码机会；
正确密码是 python123；
每次输入密码前，提示剩余尝试次数；
规则：
如果输入为空字符串 ""：提示 “密码不能为空，请重新输入”，不消耗尝试次数，继续循环（continue）
密码正确：打印 “登录成功！”，结束循环（break）
密码错误：消耗一次机会，提示密码错误
3 次机会全部用完：打印 “尝试次数耗尽，账号锁定”，程序结束。
"""

TRUE_PASSWORD="python123"
i=3
while i>0:
    password=input(f"请输入密码，您还有{i}次机会：")
    if password == "":
        print("密码不能为空，请重新输入")
        continue
    if password == TRUE_PASSWORD:
        print("登录成功！")
        break
    else:
        print("密码错误")
        i-=1
    if i==0:
        print("尝试次数耗尽，账号锁定")
        break
