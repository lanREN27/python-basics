# 2026-09-22 | W3-D7 | 错误版本，已废弃 | 覆盖边界：output 落点
# 错因：把输出文件写进了「输入素材」目录
#       RES = Path(__file__).parent / "resource" —— 这个目录的语义是输入
#       （stop_words.txt / text1.txt 都在里面）
# 报错：无 —— 静默错误。程序正常运行，结果被写到 W3/resource/result.json
# 修复：with open(Path(__file__).parent / "result.json", "w", encoding="utf-8") as f:

import sys
from collections import Counter
import jieba
from pathlib import Path
import logging
import os
import json

jieba.setLogLevel(logging.WARNING)

RES = Path(__file__).parent / "resource"

print(os.listdir(RES))
for filename in os.listdir(RES):
    print(f"{filename}: {os.path.getsize(RES / filename)}")

path = RES / "stop_words.txt"
if not path.exists():
    print("停用词表不存在")
    sys.exit(1)
stop_words = set(path.read_text(encoding="utf-8").splitlines())

path = RES / "text1.txt"
if not path.exists():
    print("文件不存在")
    sys.exit(1)
text = path.read_text(encoding="utf-8")

jieba.add_word("大模型")
words = [w for w in jieba.lcut(text) if w.isalnum() and w not in stop_words]

print("行数（含空行）：", len(text.splitlines()))
print("字符数：", len(text))
for word, cnt in Counter(words).most_common(10):
    print(f"  {word}  {cnt}")

with open(RES / "result.json", "w", encoding="utf-8") as f:   # ← 错在这里
    json.dump(Counter(words).most_common(10), f, ensure_ascii=False, indent=2)
