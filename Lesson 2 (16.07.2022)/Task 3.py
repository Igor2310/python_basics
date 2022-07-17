# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить,
# к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

time_of_year = {'spring': [1, 2, 3], 'summer': [4, 5, 6], 'fall': [7, 8, 9], 'winter': [10, 11, 12]}

while 1:
    number = int(input("Введите число от 1 до 12 "))
    if number > 0 and number <= 12:
        break

for i in time_of_year.items():
    if number in i[1]:
        print(i[0])
        break
