# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

def change_word(word_1, word_2):
    return [i[1].title() if i[0][0].isupper() else i[1] for i in zip(word_1, word_2)]


numbers = {"one": "один", "two": "два", "three": "три", "four": "четыре"}

with open("My files/text_4.txt", 'r', encoding='utf-8') as f:
    text = []
    [text.append(line) for line in f]

with open("My files/text_44.txt", 'w', encoding='utf-8') as f:
    for line in text:
        text_2 = [numbers.get(i.lower()) if i.lower() in numbers.keys() else i for i in line.split()]
        text_1 = [i for i in line.split()]
        f.write(' '.join(change_word(text_1, text_2)) + '\n')
