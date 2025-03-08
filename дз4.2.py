import random

my_list = [0, 1, 7, 2, 4, 8]
my_list2 = [1, 3, 5]
my_list3 = [6]
my_list4 = []

NUMS_SIZE = 10
my_list5 = []   # проверка работоспособности кода с помощью модуля random
for j in range(NUMS_SIZE):
    my_list5.append(random.randint(1, 10))

for_for = my_list, my_list2, my_list3, my_list4, my_list5

nums = 0
for row in for_for:
    for i in range(0, len(row), 2):
        nums += row[i]
    if len(row) == 1:
        res = row[-1]
        print(f"{row} => {res ** 2}")
    elif not row == list():
        print(f"{row} => {nums * row[-1]}")
    else:
        print(f"{row} => 0")
    nums = 0

