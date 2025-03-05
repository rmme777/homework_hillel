list1 =[1, 5, 3, 8, 9, 11] # [1, 5, 3, 8, 9, 11] => [[1, 5, 3], [8, 9, 11]]
list2 = [6, 5, 2] # [6, 5, 2] => [[6, 5], [2]]
list3 = [1] # [1] => [[1], []]
list4 = [] # [] => [[], []]

for_if = list1 # просто по очереди присваиваю списки 1, 2, 3, 4 чтобы не дублировать код
mid = len(for_if) // 2
if len(for_if) % 2 != 0:
    mid += 1

first_half = for_if[:mid]
second_half = for_if[mid:]

if len(for_if) % 2 == 0:
    print(f"{for_if} => [{first_half}, {second_half}]")
elif first_half > second_half or first_half < second_half:
    print(f"{for_if} => [{first_half}, {second_half}]")
elif mid == 0:
    print(f"{for_if} => [{for_if}, []]")
