import re
def extract_error_log(log_file_path, output_path):
    # 任务1：创建列表保存错误信息，计数器
    error_list = []
    level_count = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    # 任务2：打开日志文件，用enumerate读取行号+内容
    with open(log_file_path,"r",encoding="utf-8") as f:
        for line_num,line in enumerate(f,start=1):
            if 'ERROR' in line :
                error_list.append((line_num,line.strip()))
                level_count["ERROR"] += 1
            elif 'WARNING' in line :
                level_count["WARNING"] += 1
            elif 'INFO' in line :
                level_count["INFO"] += 1
        print(level_count)


    # 任务4：统计错误总数
    len_error = len(error_list)
    print(f"一共发现 {len_error} 条ERROR日志")
    # 任务5：控制台打印前3条错误
    print("====前3条错误====")
    for idx,(num,content) in enumerate(error_list[:3],start=1):
        print(f"{num} | {content}")

    # 任务6：写入文件到 output_path

    with open(output_path,"w",encoding="utf-8") as f_out:

        f_out.write("行号\t日志内容\n")
        for line_num,content in error_list:
            f_out.write(f"{line_num}\t{content}\n")

if __name__ == "__main__":
    log_path = "resource/sample.log"
    out_path = "resource/error_log.txt"
    extract_error_log(log_path, out_path)