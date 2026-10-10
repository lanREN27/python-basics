# ============================================================
# ⚠️ 不合格版本 —— 保留作对照，勿直接使用
# ------------------------------------------------------------
# 日期：2026-09-19
# 问题：数的是「字母」不是「词」—— 做的是字符级统计，不是词级统计
#       实测输出 [('e',93),('t',74),...]，全是单个字母
# 根因：没有分词，直接按字符遍历（char.isalpha() + char_count[char]）
# 达标版本：W2/词频统计加深.py（用 jieba 分词）
# 标注日期：2026-10-02（W1–W4 对账时实测发现）
# 标注原因：不合格版本留在原地不标注 → 下次翻到它的人会以为它是对的
# ============================================================

def top_word(char_count:dict,n:int)->list:
    sort_char_count = sorted(char_count.items(),key=lambda item:item[1],reverse=True)
    return sort_char_count[:n]
def char_count_fun(sentence)->list :
    char_count={}
    for char in sentence:
        if char.isalpha():
            char_count[char] = char_count.get(char,0)+1
    return top_word(char_count,10)

with open("resource/text.txt","r",encoding="utf-8") as f:
    sentence = f.read()
    print(sentence)

print(char_count_fun(sentence))

with open("resource/output.txt","w",encoding="utf-8") as f:
    f.write(str(char_count_fun(sentence)))

