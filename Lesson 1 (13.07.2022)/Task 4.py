# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("enter a positive integer "))
max_number = 0

while number:
    a = number % 10
    number //= 10
    if max_number < a:
        max_number = a

print(max_number)
