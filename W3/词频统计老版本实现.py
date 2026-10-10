

with open("resource/text1.txt","r",encoding="utf-8") as f:
    text = f.read()

# stop_words = {"的", "是", "可以", "也", "来","做","一门", "我们", "and", "or", "but", "so", "because", "although", "if", "when", "where", "who", "what", "why", "how"}

dic_char ={}
for char in text :
    if char.isalpha() :
        dic_char[char] = dic_char.get(char,0)+1
sorted_dic_char = sorted(dic_char.items(),key= lambda item:item[1])

print(sorted_dic_char[0:10])