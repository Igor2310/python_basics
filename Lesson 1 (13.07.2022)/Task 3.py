# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


n = input("enter number ")

nn = n + n
nnn = nn + n

print(int(n) + int(nn) + int(nnn))
