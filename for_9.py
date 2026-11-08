# Задание 9 (Дан список чисел. Найдите наибольший элемент, не используя max())
numbers = [3, 7, 2, 9, 4]
bol = numbers[0]
for num in numbers:
    if num > bol:
        bol = num
print(bol)
