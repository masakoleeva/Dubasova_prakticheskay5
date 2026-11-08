# Задание 8 (Дана строка. Посчитайте, сколько в ней гласных букв)
text = "это задание восемь"
gl = "аеёиоуыэюя"
count = 0
for x in text:
    if x in gl:
        count += 1
print(count)
