# # 使用大括号 {} 来创建空字典
# emptyDict = {}
#
# # 打印字典
# print(emptyDict)
#
# # 查看字典的数量
# print(f"Length:{len(emptyDict)}")
#
# # 查看类型
# print(type(emptyDict))
#
# # !/usr/bin/python3
#
# tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#
# print(f"tinydict['Name']: {tinydict['Name']}")
# print(f"tinydict['Age']: {tinydict['Age']}")
#
# tinydict['qiukang']='niubi'
# print(tinydict)
# print(tinydict['qiukang'])
#
# del tinydict['Name']
# print(tinydict)
#
# # !/usr/bin/python3
#
# # tinydict = {['Name']: 'Runoob', 'Age': 7}#TypeError: unhashable type: 'list'
#
# # print("tinydict['Name']: ", tinydict['Name'])


# x = True
# country_counter = {}

# def addone(country):
#     if country in country_counter:
#         country_counter[country] += 1
#     else:
#         country_counter[country] = 1
#     print(country_counter)
#
# addone('China')
# addone('Japan')
# addone('china')
#
# print(len(country_counter))
# print(country_counter)

# confusion = {}
# confusion[1] = 1
# confusion['1'] = 2
# confusion[1] += 1
#
# sum = 0
# for k in confusion:
#     sum += confusion[k]
#
# print(sum)
#
# dct1 = {'邱康':8,
#         '张三':9,
#         '李四':7,
#         '王五':6
#         }
