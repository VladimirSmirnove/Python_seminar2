# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов введеных пользователем. 
from re import M


#N = int(input("Введите число: "))
#N_list = list(range(-N, N+1))
#mult = 1
#for i in range(len(N_list)):
##    i = int(input("Введите позицию i"))
#for j in range(len(N_list)):
#    j = int(input("Введите позицию"))
#mult=i*j
#print("Индекс: ", i,"Элемент по индексу: ", N_list[i],"Произведение элементов: ", mult, j)


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
