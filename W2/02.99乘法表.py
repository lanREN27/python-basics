def print_multiplication_table():
    for i in range(1,10):
        for j in range(1,i+1):
            print(f"{j}*{i}={i*j}",end=" ")#打印乘法表，end=" "表示不换行
        print()
print_multiplication_table()
        