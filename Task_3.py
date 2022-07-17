# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
from re import A


N = int(input("Введите число: "))
sum = 0
for i in range(1,N+1):
    a = (1 + (1/i))**i
    sum += a
    print(i,":", sum)  


