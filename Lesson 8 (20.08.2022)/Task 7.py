# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} + {self.b}i"

    def __add__(self, other):
        return ComplexNumber((self.a + other.a), (self.b + other.b))

    def __mul__(self, other):
        return ComplexNumber((self.a * other.a - self.b * other.b), (self.a * other.b + self.b * other.a))


number1 = ComplexNumber(3, 1)
print(number1)
number2 = ComplexNumber(2, -3)
print(number1 + number2 + number1)
print(number1 * number2)
print(number1 * number2 * number1)
