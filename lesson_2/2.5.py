rating = [2, 3, 1, 5, 3, 9, 0]
while True:
    rating.append(int(input('Введите новый элемент рейтинга: ')))
    b = sorted(rating)
    print(b[::-1])