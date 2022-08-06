# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.


def my_f(number_1, number_2, number_3):
    try:
        number_1 = float(number_1)
        number_2 = float(number_2)
        number_3 = float(number_3)
        return sum(sorted([number_1,number_2,number_3])[:-1])
    except ValueError as err:
        print(err)


numbers=[]
for i in range(0,3):
     numbers.append(input(f"Введитете число {i+1}) "))
print(my_f(numbers[0],numbers[1],numbers[2]))


