# Создать текстовый файл (не программно). Построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк). Определить,
# кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:

# Иванов 23543.12
# Петров 13749.32

with open("My files/text_3.txt", 'r', encoding='utf-8') as f:
    print("Employees who earn less than 20,000")
    employees = {line.split()[0]: line.split()[1] for line in f.readlines()}
    [print(i[0]) for i in employees.items() if float(i[1]) < 20000]

    print("-" * 50)
    print(f"Mean salary of employees {sum([float(i) for i in employees.values()]) / len(employees)}")
