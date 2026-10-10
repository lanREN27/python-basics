"""
词频统计Counter实现:用于统计中文词频

"""
from collections import Counter
import string
import jieba
jieba.setLogLevel(jieba.logging.INFO)
jieba.add_word("大模型")

stop_words = {"的", "是", "可以", "也", "来","做","一门", "我们", "and", "or", "but", "so", "because", "although", "if", "when", "where", "who", "what", "why", "how"}
with open("resource/text1.txt","r",encoding="utf-8") as f :
    text = f.read()

words = jieba.lcut(text)

punctuation = set(string.punctuation + "，。、：；？！“”（）【】……——\n\t")
filter_words = [word for word in words if word.isalnum() and word.strip() and word not in stop_words]
counter_word = Counter(filter_words)

print(counter_word.most_common(10))
print('。'.isalnum())
print('大模型'.isalnum())
print('A1'.isalnum())
print(''.isalnum())