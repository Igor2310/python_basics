# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма. Например, прибыль — выручка больше издержек,
# или убыток — издержки больше выручки.
#
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль фирмы
# в расчёте на одного сотрудника.


income = int(input("enter income in rubles "))
expenses = int(input("enter expenses in rubles "))

if income > expenses:
    print("income is more than expenses")
    profit = income - expenses
    print(f"profit = {profit} rubles")
    number_of_employees = int(input("enter number of employees "))
    profit_per_employee = profit / number_of_employees
    print(f"profit per one employee {profit_per_employee:.2f} rubles")

elif income < expenses:
    print("income is less than expenses")
else:
    print("income equals to expenses")
