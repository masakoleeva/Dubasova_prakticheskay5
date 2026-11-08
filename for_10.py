# Задание 10 (Выведите таблицу умножения от 1 до 9 в виде квадрата)
for i in range(1, 10):
    for y in range(1, 10):
        print(i * y, end=" ")
    print()
