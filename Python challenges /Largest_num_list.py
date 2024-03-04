def largest_num(list):
    return max(list)


def largest_num_manual(list):
    num = list[0]
    for x in list:
        if x > num:
            num = x
    return num


print(largest_num_manual([1, 21, 32, 46, 234, 1234321, 3234, 234, 324356, 323, 44, 9999, 999999997]))
print(largest_num([1, 21, 32, 46, 234, 1234321, 3234, 234, 324356, 323, 44, 9999, 999999997]))
