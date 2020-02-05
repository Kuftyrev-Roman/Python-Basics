from itertools import count

for i in count(3):
    if i > 10:
        break
    else:
        print(i)
