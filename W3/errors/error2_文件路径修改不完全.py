# 2026-09-22 | W3-D7 异常处理 | 错误版本（已废弃）| 覆盖边界：无
# 错因：只改了 path = Path(...) 两处，漏改 os.listdir 的 3 处相对路径
# 报错：FileNotFoundError: [WinError 3] 系统找不到指定的路径。: 'resource/'
#       触发条件：工作目录 ≠ W3（例如 cd E:\PythonProject1 后再运行）
# 修复：把 os.listdir("resource/") 也改成 os.listdir(RES)，RES = Path(__file__).parent / "resource"

import sys
from collections import Counter
import jieba
from pathlib import Path
import logging
import os
import json

jieba.setLogLevel(logging.WARNING)

# ① 停用词表
print(os.listdir("resource/"))                                        # ← 漏改（崩在这行）
for filename in os.listdir("resource/"):                              # ← 漏改
    print(f"{filename}: {os.path.getsize('resource/' + filename)}")   # ← 漏改

path = Path(__file__).parent / "resource" / "stop_words.txt"          # ← 已改
if not path.exists():
    print("停用词表不存在")
    sys.exit(1)
stop_words = set(path.read_text(encoding="utf-8").splitlines())

# ② 目标文件
path = Path(__file__).parent / "resource" / "text1.txt"               # ← 已改
if not path.exists():
    print("文件不存在")
    sys.exit(1)
text = path.read_text(encoding="utf-8")

# ③ 业务逻辑
jieba.add_word("大模型")
words = [w for w in jieba.lcut(text) if w.isalnum() and w not in stop_words]

# ④ 输出
print("行数（含空行）：", len(text.splitlines()))
print("字符数：", len(text))
for word, cnt in Counter(words).most_common(10):
    print(f"  {word}  {cnt}")

with open("result.json", "w", encoding="utf-8") as f:                 # ← 漏改
    json.dump(Counter(words).most_common(10), f, ensure_ascii=False, indent=2)
