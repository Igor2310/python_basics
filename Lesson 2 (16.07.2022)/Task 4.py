# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать. Если слово длинное,
# выводить только первые 10 букв в слове.

sentence = input("Введите строку ")

for i in enumerate(sentence.split(), 1):
    print(f"{i[0]}) {i[1][:10]}")
