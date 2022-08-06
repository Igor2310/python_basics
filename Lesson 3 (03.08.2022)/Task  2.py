# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.


def my_f(name, surname, year_birth, city, email, phone_number):
    print(f"{name} , {surname} , {year_birth}, {city}, {email}, {phone_number}", )


# position arguments (позиционные аргументы)
my_f("Igor", "Nikolaev", 1986, "Moscow", "NikilaevIgor1986@gmail.com", "+79483055634")
# keyword arguments (именованные аргументы)
my_f(surname="Watson", city="London", email="WKate1990.com", phone_number="+02023123465", name="Kate", year_birth=1990)
