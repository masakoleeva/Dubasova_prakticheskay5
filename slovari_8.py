# Задание 8 (Дана строка из слов через пробел. Посчитайте, сколько раз встречается каждое слово, и выведите самое частое)
text = "кот пёс кот птица кот пёс"
sp = text.split()
slov = {}
for x in sp:
    if x in slov:
        slov[x] += 1
    else:
        slov[x] = 1
print(max(slov, key=slov.get))
