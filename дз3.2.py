# Версия 1
my_list = [1, 3, 9, 4]
my_list_copy = my_list.copy()
deleted_num1, deleted_num2, deleted_num3 = my_list.pop(0), my_list.pop(0), my_list.pop(0)
my_list.append(deleted_num1)
my_list.append(deleted_num2)
my_list.append(deleted_num3)
print(f"{my_list_copy} => {my_list}")

# Версия 2
new_list = [4, 5, 2]
new_list_copy = new_list.copy()
last_dig = new_list.pop(-1)
new_list.insert(0, last_dig)
print(f"{new_list_copy} => {new_list}")
