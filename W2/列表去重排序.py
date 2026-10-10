def remove_duplicates_and_sort(lis1:list)->list:
    return sorted(list(set(lis1)))
lis1 = [1,2,3,5,5,5,4,6,1,8,9,7,5,4,8,164,16,6,65,23,1,1616,8,86,1,1,13,13,165,16,146,464]
print(remove_duplicates_and_sort(lis1))

