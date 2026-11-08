# Задание 10 (Программа загадывает число от 1 до 100. Пользователь угадывает его, а программа отвечает «больше» или «меньше». В конце выведите количество попыток)
import random

target = random.randint(1, 100)
guess = 0
attempts = 0
while guess != target:
    guess = int(input("Угадайте число: "))
    attempts += 1
    if guess < target:
        print("Больше")
    elif guess > target:
        print("Меньше")
print(attempts)
