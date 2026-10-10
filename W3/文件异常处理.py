# import pathlib
import sys
from collections import Counter
import jieba
from pathlib import Path
import logging
import os
import json

jieba.setLogLevel(logging.WARNING)
RES = Path(__file__).parent / "resource"

# ① 停用词表 —— 也要保护
print(os.listdir(RES))
for filename in os.listdir(RES):
    print(f"{filename}: {os.path.getsize(RES / filename)}")
path = RES / "stop_words.txt"
if not path.exists():
    print("停用词表不存在")
    sys.exit(1)
stop_words = set(path.read_text(encoding="utf-8").splitlines())

# ② 目标文件 —— try 只包 open
path = RES / "text1.txt"


if not path.exists():
    print("文件不存在")
    sys.exit(1)
text = path.read_text(encoding="utf-8")


# ③ 业务逻辑在 try 外 —— 这里出 bug 就该崩
jieba.add_word("大模型")
words = [w for w in jieba.lcut(text) if w.isalnum() and w not in stop_words]

# ④ 输出
print("行数（含空行）：", len(text.splitlines()))
print("字符数：", len(text))
for word, cnt in Counter(words).most_common(10):
    print(f"  {word}  {cnt}")

with open(Path(__file__).parent / "result.json", "w", encoding="utf-8") as f:
    json.dump(Counter(words).most_common(10), f, ensure_ascii=False, indent=2)
