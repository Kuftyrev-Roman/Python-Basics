from itertools import cycle

с = 0
for i in cycle("CYCLE"):
    if с > 10:
        break
    else:
        print(i)
        с += 1
