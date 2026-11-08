# Задание 7 (Дан список чисел. Посчитайте, сколько в нём положительных чисел)
numbers = [3, -5, 7, -2, 9, -1]
count = 0
for num in numbers:
    if num > 0:
        count += 1
print(count)
