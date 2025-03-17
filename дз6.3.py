enter_num = input("Введите число: ")
nums_proces = list(enter_num)
nums_list = []
nums_cicle = 0

while True:
    nums_cicle = 1
    for i in nums_proces:
        nums_list.append(int(i))

    for j in nums_list:
        nums_cicle *= j

    nums_proces.clear()

    for k in str(nums_cicle):
        nums_proces.append(int(k))
    nums_list.clear()
    if nums_cicle <= 9:
        break
print(nums_cicle)
