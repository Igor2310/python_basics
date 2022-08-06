# 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
# сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().


# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = input(f"{i + 1}) ")
    lst.append(ele)  # adding the element

for i in range(0, n, 2):
    if i == n - 1 and n % 2 == 1:
        break
    a = lst[i]
    lst[i] = lst[i + 1]
    lst[i + 1] = a

print(lst)
