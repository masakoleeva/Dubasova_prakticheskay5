# Задание 9 (Дан словарь. Создайте новый словарь, в котором ключи и значения поменяны местами)
slov = {"a": 1, "b": 2, "c": 3}
new_slov = {}
for key in slov:
    new_slov[slov[key]] = key
print(new_slov)
