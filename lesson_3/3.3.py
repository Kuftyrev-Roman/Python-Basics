def my_func(arg_1, arg_2, arg_3):
    sorted_num = sorted([arg_1, arg_2, arg_3], reverse=True)
    return sorted_num[0] + sorted_num[1]
    
print(my_func(1, 2, 3))