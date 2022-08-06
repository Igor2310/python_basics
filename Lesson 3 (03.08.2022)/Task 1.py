# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_f(dividend, divisor):
    try:
        print(float(dividend) / float(divisor))
    except ZeroDivisionError as err:
        print(err)
    except ValueError as err:
        print(err)


my_f(input("Введитете делимое "), input("Введитете делитель "))
