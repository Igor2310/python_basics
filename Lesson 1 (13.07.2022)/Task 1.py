# 1. Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.

name = "Andy"
last_name = "Craft"
age = 29
isMarried = False
height = 178.2
weight = 71

print(name, last_name, age, isMarried, height, weight)

name = input("Insert name ")
age = int(input("Insert age "))
isMarried = bool(int(input("Marital status (0 - False or 1 - True) ")))

print(name, age, isMarried)
