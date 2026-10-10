def isPalindrome(self, x: int) -> bool:
    x = str(x)
    len_x = len(x)
    for i in x :
        if i !=x[len_x-1]:
            return False
        len_x -=1

    return True

x = input("请输入一个数字：")
print(isPalindrome(1, x))
