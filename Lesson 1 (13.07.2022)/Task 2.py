# Пользователь вводит время в секундах. Переведите время
# в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
import time

seconds = int(input("enter number of seconds "))

hours = seconds // 3600
minutes = seconds // 60 - hours * 60
sec = seconds % 60
hours %= 24

print(f"{hours:02d}:{minutes:02d}:{sec:02d}")

print("Control")
print(time.strftime('%H:%M:%S', time.gmtime(seconds)))
