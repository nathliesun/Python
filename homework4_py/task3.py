from enum import unique
from random import randrange

def count_of_numbers(count: int):
    if count < 0:
        print("отрицательное число элементов!")
        return[]
    list_numbers = []
    for i in range(count):
        list_numbers.append(randrange(count))
    return list_numbers

def non_repeat_elements(list_numbers):
    return set(list_numbers)

all_list = count_of_numbers(int(input("Размер списка: ")))
print(all_list)
print(non_repeat_elements(all_list))
