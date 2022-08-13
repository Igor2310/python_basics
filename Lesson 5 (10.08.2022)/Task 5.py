# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле
# и выводить её на экран.

with open("My files/text_5.txt", 'r', encoding='utf-8') as f:
    try:
        if len(f.readlines()) == 1:
            f.seek(0)
            print(sum(float(i) for i in f.readline().split(" ")))
        else:
            print("В файле должно быть заполнена одна строка")
    except(ValueError) as Error:
        print(Error)
