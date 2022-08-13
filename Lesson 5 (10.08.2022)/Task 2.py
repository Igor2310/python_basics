# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

# space in the beginning and the end line are not considered
with open("My files/text_2.txt", 'r', encoding='utf-8') as f:
    count = 0
    for line in f.readlines():
        count += 1
        line = line.strip()
        print(f"line {count} has {len(line)} symbols ")
