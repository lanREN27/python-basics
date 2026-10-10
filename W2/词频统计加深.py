import re
import os


def count_english_word_frequency(file_path, top_n=10):
    # 停用词文件路径
    stop_word_path = "resource/stop_words.txt"

    # 读取停用词
    with open(stop_word_path, "r", encoding="utf-8") as f:
        stop_words = {line.strip() for line in f.read().splitlines()}

    word_count = {}

    # 读取目标文本
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.lower()
            # 正则清除标点
            line = re.sub(r'[^\w\s]', '', line)
            words = line.split()
            for word in words:
                if word not in stop_words:
                    word_count[word] = word_count.get(word, 0) + 1

    # 排序
    sorted_count_word = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

    # 输出topN
    print(f"\nTop {top_n}高频单词：")
    for idx, (word, cnt) in enumerate(sorted_count_word[:top_n], start=1):
        print(f"{idx}. {word}: {cnt}")

    # 自动创建resource文件夹，不存在就新建
    os.makedirs("resource", exist_ok=True)
    # 写入全部结果
    with open("resource/english_word_result.txt", "w", encoding="utf-8") as f:
        f.write("单词\t次数\n")
        for word, count in sorted_count_word:
            f.write(f"{word}\t{count}\n")


# ========== 调用入口 ==========
if __name__ == "__main__":
    # 【测试：可以直接写绝对路径，先绕过相对路径问题】
    # file_path = r"E:\PythonProject1\W2\resource\text.txt"
    # stop_word_path = r"E:\PythonProject1\W2\resource\stop_words.txt"

    file_path = "resource/text.txt"
    count_english_word_frequency(file_path)