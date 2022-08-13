# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчёт средней
# прибыли её не включать. Далее реализовать список. Он должен содержать словарь
# с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json

with open("My files/text_7.txt", 'r', encoding='utf-8') as f:
    lst = [i.split() for i in f.readlines()]

firms = {i[0]: float(i[2]) - float(i[3]) for i in lst}
positive_revenue = [i[1] for i in firms.items() if i[1] > 0]
average_revenue = {"average_profit": sum(positive_revenue) / len(positive_revenue)}
result = [firms, average_revenue]

# Serializing json
json_object = json.dumps(result, indent=4, ensure_ascii=False)

# Writing to sample.json
with open("My files/text_777.json", 'w', encoding='utf-8') as f:
    f.write(json_object)
