# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.


class DivideByZero(Exception):
    def __init__(self):
        super().__init__("Делить на ноль нельзя")


dividend = 5
divider = 0

try:
    if divider == 0:
        raise DivideByZero()
    print(f"{dividend / divider:.2f}")

except Exception as err:
    print(err)
