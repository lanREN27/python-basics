import sys
from collections import Counter
import jieba
from pathlib import Path
import logging
import os
import json

jieba.setLogLevel(logging.WARNING)

# ① 停用词表 —— 也要保护
print(os.listdir("resource/"))
for filename in os.listdir("resource/"):
    print(f"{filename}: {os.path.getsize('resource/' + filename)}")

path = Path("resource/stop_words.txt")
if not path.exists():
    print("停用词表不存在")
    sys.exit(1)
stop_words = set(path.read_text(encoding="utf-8").splitlines())
# except FileNotFoundError as e:
#     print(f"停用词表不存在：{e}")
#     sys.exit(1)

# ② 目标文件 —— try 只包 open
path = Path("resource/text1.txt")

if not path.exists():
    print("文件不存在")
    sys.exit(1)
text = path.read_text(encoding="utf-8")
#         text = f.read()
# except FileNotFoundError as e:
#     print(f"文件不存在：{e}")
#     sys.exit(1)

# ③ 业务逻辑在 try 外 —— 这里出 bug 就该崩
jieba.add_word("大模型")
words = [w for w in jieba.lcut(text) if w.isalnum() and w not in stop_words]

# ④ 输出
print("行数（含空行）：", len(text.splitlines()))
print("字符数：", len(text))
for word, cnt in Counter(words).most_common(10):
    print(f"  {word}  {cnt}")

# dic_words = dict(Counter(words).most_common(10))
# counter = Counter(words)
with open("result.json", "w", encoding="utf-8") as f:
    json.dump(Counter(words).most_common(10), f, ensure_ascii=False, indent=2)
