# Реализуйте алгоритм перемешивания списка.
from ast import For
import random

List_1 = [1,2,3,4,5,66]
List_2 = []
print("\nНачальный список:\n", List_1)
for i in range(10):
    random.shuffle(List_1)
    List_2.append(List_1.copy())
print ("Перемешанный список:\n",List_1)

