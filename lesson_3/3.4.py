def my_func(x, y):
    i = 0
    mult = 1
    while i < abs(y):
        mult = mult * x
        i += 1
    exp = 1 / mult    
    return exp
    
print(my_func(2, -3))