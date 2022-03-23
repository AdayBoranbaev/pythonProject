#-------------#1--------------------
from sys import argv

time, bid, premium = map(float, argv[1: ])
print(f" Результат: - {time * bid + premium}")

#------------#2---------------------

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f"Исходный список: {my_list}")
new_list = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(f"Новый список: {new_list}")

#------------#3----------------------

my_list = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(my_list)

#------------#4---------------------

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f"Исходный список: {my_list}")
new_list = [el for el in my_list if my_list.count(el) == 1 ]
print(f"Новый список: {new_list}")

#------------#5---------------------

from functools import reduce

def my_list(n, m):
    return n * m

new_list = [el for el in range(100, 1000, 2)]
print(f"Результат вычисления произведения всех элементов списка: {reduce(my_list, new_list)}")

#-------------#6--------------------------

from itertools import count, cycle

my_count = count(5)
my_cycle = cycle("zxc")

for n in range(10):
    print("(my_count, my_cycle) = ({}, {})". format(next(my_count), next(my_cycle)))

#------------#7---------------------------

def factoial(number):
    f_num = 1
    for i in range(number + 1):
        yield f'{i}!= {f_num}'
        f_num *= i + 1


for el in factoial(int(input('Результат: '))):
    print(el)