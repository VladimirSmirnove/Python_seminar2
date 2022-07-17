# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов введеных пользователем. 
from re import M


M = int(input("Введите число: "))
lst = list(range(-M,M))
multi=0
for i in lst:
    i = int(input("Введите первый индекс элемента: "))
    break
print(lst[i])
for j in lst:
    j = int(input("Введите второй индекс элемента: "))
    break
print(lst[j])
mult = lst[i]*lst[j]
print("Произведение элементов: ", mult)
