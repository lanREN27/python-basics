def find_max(lst):
    if not lst:
        return None
    need_max = lst[0]
    for i in lst:
        if i>need_max:
            need_max = i
    return need_max

list1 = [1,2,3,4,5,6,7,8,9]
print(find_max(list1))



