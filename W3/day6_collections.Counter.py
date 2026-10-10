#命名元组：namedtuple
# from collections import namedtuple
#
# Person = namedtuple("Person",["name","age"])
# man = Person(name="小甲鱼",age=18)
# print(man.name,man.age)


#Counter类：用于存储元素以及出现的数量
# from collections import Counter
# text = "I love qiukang "
# counter = Counter(text)
# print(counter.most_common(2))

# import string
# import jieba
#
#
# jieba.setLogLevel(jieba.logging.INFO)
#
# stop_words={"牛","逼"}
# stop = set(string.punctuation+"，"+"的")
# text = "宇宙无敌大爆炸,史上最牛逼的电影"
# words = jieba.lcut(text)
# print(words)
# l_words = [word for word in words if word not in stop and word not in stop_words]
# print(l_words)

from collections import Counter
s = "ehijk"
t = "hijke"
counter = Counter(s)
counter2 = Counter(t)

print(counter)
print(counter2)
if counter == counter2:
    print("yes")
else:
    print("no")
