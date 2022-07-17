# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами, то есть характеристиками товара: название, цена,
# количество, единица измерения. Структуру нужно сформировать программно, запросив все данные у пользователя.

base_date = []
quantity_of_goods = int(input("Число товаров, которые вы хотите добавить: "))
my_set={"название","цена","количество","eд"}

for i in range(1, quantity_of_goods+1):
    print(f"товар №{i}")
    name = input("название: ")
    price = float(input("цена: "))
    quantity = int(input("количество: "))
    unit = input("eд: ")
    base_date.append((1, {"название": name, "цена":price, "количество": quantity, "eд": unit}))


lst=[]
while True:
    parameter = input("Введите ключ товара: ")
    if parameter in my_set:
        break
    else:
        print("Ключ товара не найдет, введите снова")

for i in base_date:
    lst.append((i[1].get(parameter)))
lst=list(dict.fromkeys(lst))

print(f"{parameter}: {lst}")

